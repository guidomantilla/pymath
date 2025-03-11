from IPython.display import Latex, display
from sympy import latex
from sympy.logic.boolalg import truth_table


def print_latex(expr, key: str = None):
    expression = "$$\\Huge {}$$".format(latex(expr))
    if key is not None:
        expression = "$$\\Huge {}: {}$$".format(key, latex(expr))
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
