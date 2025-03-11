from typing import List

import sympy as sp
from sympy.core.relational import Relational
from typing_extensions import Any

from pkg.logica.functions import print_latex


def add_many(r: List[Relational]) -> Relational:
    if len(r) < 2:
        raise ValueError("At least 2 relational expression are required")

    accum = r[0]
    for rel in r[1:]:
        accum = add(accum, rel)

    return accum


def add(p: Relational, q: Relational, latex=False, debug=False) -> Relational:
    relational_operator = check_relations_operator(p, q)

    lhs_sum = sp.Add(p.lhs, q.lhs, evaluate=False)
    rhs_sum = sp.Add(p.rhs, q.rhs, evaluate=False)
    sum = relational_operator(lhs_sum, rhs_sum)

    if latex:
        print_latex(sum)
        print_latex(sum.evalf())
        print_latex(sum.simplify())

    if debug:
        print(f"sum: {sum}")
        print(f"sum: {sum.evalf()}")
        print(f"sum: {sum.simplify()}")

    return sum.simplify()


"""


"""


def transitive_many(r: List[Relational]) -> Relational:
    if len(r) < 2:
        raise ValueError("At least 2 relational expression are required")

    accum = r[0]
    for rel in r[1:]:
        accum = transitive(accum, rel)

    return accum


def transitive(p: Relational, q: Relational, latex=False, debug=False) -> Relational:

    p, q = check_transitive(p, q)
    relational_operator = check_relations_operator(p, q)

    ab_sum = relational_operator(p.lhs - p.rhs, p.rhs - p.rhs)
    bc_sum = relational_operator(q.lhs - q.rhs, q.rhs - q.rhs)

    if latex:
        print_latex(ab_sum)
        print_latex(bc_sum)

    if debug:
        print(f"ab_sum: {ab_sum}")
        print(f"bc_sum: {bc_sum}")

    return add(p, q, latex, debug)


"""


"""


def check_transitive(p: Relational, q: Relational) -> [Relational, Relational]:
    if p.rhs.equals(q.lhs):
        return p, q

    if q.rhs.equals(p.lhs):
        return q, p

    raise TypeError("expressions are not transitives")


def check_relations_operator(p: Relational, q: Relational) -> Any:
    valid_relation = {
        sp.Equality: sp.Equality,
        sp.StrictGreaterThan: sp.StrictGreaterThan,
        sp.StrictLessThan: sp.StrictLessThan,
    }

    if p.__class__ not in valid_relation or q.__class__ not in valid_relation:
        raise TypeError("expressions must be one of (==, <, >)")

    if p.__class__ is sp.StrictGreaterThan and q.__class__ is sp.StrictLessThan:
        raise TypeError("expressions are not transitives")

    if p.__class__ is sp.StrictLessThan and q.__class__ is sp.StrictGreaterThan:
        raise TypeError("expressions are not transitives")

    if p.__class__ is sp.StrictGreaterThan or p.__class__ is sp.StrictLessThan:
        return p.__class__

    if q.__class__ is sp.StrictGreaterThan or q.__class__ is sp.StrictLessThan:
        return q.__class__
