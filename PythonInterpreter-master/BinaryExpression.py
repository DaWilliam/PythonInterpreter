from ArithmeticOperator import ArithmeticOperator
from ArithmeticExpression import ArithmeticExpression


class BinaryExpression(ArithmeticExpression):
    op = None
    expr1 = None
    expr2 = None

    def __init__(self, op, expr1, expr2):
        if op is None:
            raise Exception("null arithmetic operator argument")
        if expr1 is None or expr2 is None:
            raise Exception("null arithmetic expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        value = 0

        if self.op == ArithmeticOperator.ADD_OP:
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == ArithmeticOperator.SUB_OP:
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op == ArithmeticOperator.MUL_OP:
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == ArithmeticOperator.DIV_OP:
            value = self.expr1.evaluate() / self.expr2.evaluate()

        return value
