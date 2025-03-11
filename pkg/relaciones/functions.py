from typing import List

import sympy as sp
from sympy.core.relational import Relational

from pkg.logica.functions import print_latex


def add_many(r: List[Relational]) -> Relational:
    if len(r) < 2:
        raise ValueError("At least 2 relational expression are required")

    sum = r[0]
    for rel in r[1:]:
        sum = add(sum, rel)

    return sum


def add(p: Relational, q: Relational, latex=False, debug=False) -> Relational:

    if p.__class__ != q.__class__:
        raise TypeError("Both relational expression must be of the same type")

    relational_operator = p.__class__

    ab_sum = relational_operator(p.lhs - p.rhs, p.rhs - p.rhs)
    bc_sum = relational_operator(q.lhs - q.rhs, q.rhs - q.rhs)

    lhs_sum = sp.Add(ab_sum.lhs, bc_sum.lhs, evaluate=False)
    rhs_sum = sp.Add(ab_sum.rhs, bc_sum.rhs, evaluate=False)
    sum = relational_operator(lhs_sum, rhs_sum)

    if latex:
        print_latex(ab_sum)
        print_latex(bc_sum)
        print_latex(sum)
        print_latex(sum.evalf())
        print_latex(sum.simplify())

    if debug:
        print(f"ab_sum: {ab_sum}")
        print(f"bc_sum: {bc_sum}")
        print(f"sum: {sum}")
        print(f"sum: {sum.evalf()}")
        print(f"sum: {sum.simplify()}")

    return sum.simplify()


def transitive_many(r: List[Relational]) -> Relational:
    if len(r) < 2:
        raise ValueError("At least 2 relational expression are required")

    sum = r[0]
    for rel in r[1:]:
        sum = transitive(sum, rel)

    return sum


def transitive(p: Relational, q: Relational, latex=False, debug=False) -> Relational:

    if not p.rhs.equals(q.lhs):
        raise TypeError(
            "Both relational expression must be ready for transitive operation"
        )

    return add(p, q, latex, debug)
