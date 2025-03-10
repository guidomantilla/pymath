import sympy as sp
from sympy import latex
from IPython.display import display, Latex
from sympy.logic.boolalg import truth_table


def print_latex(expr):
    expression = "$$\\Huge {}$$".format(latex(expr))
    display(Latex(expression))


def print_truth_table(expr, symbols):
    atoms = ",".join(map(str, symbols))
    table = truth_table(expr, symbols)
    for t in table:

        inputs = ""
        for i in t[0]:
            inputs += str(bool(i)) + ","
        inputs = inputs[:-1]

        template = "$$\\large {}({}) \\Rightarrow {}({})$$"
        expression = template.format(atoms, inputs, latex(expr), latex(t[1]))
        display(Latex(expression))
