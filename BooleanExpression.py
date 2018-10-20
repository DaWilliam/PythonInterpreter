from RelationalOperator import RelationalOperator

class BooleanExpression:

    op = None

    expr1 = None
    expr2 = None

    def __init__(self, op, expr1, expr2):
        if op == None:
            raise Exception("null relational operator argument")
        if expr1 == None or expr2 == None:
            raise Exception ("null arithmetic expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        result = False
        if self.op == RelationalOperator.EQ_OP:
            result = (self.expr1.evaluate() == self.expr2.evaluate())
        elif self.op == RelationalOperator.NE_OP:
            result = (self.expr1.evaluate() != self.expr2.evaluate())
        elif self.op == RelationalOperator.LT_OP:
            result = (self.expr1.evaluate() < self.expr2.evaluate())
        elif self.op == RelationalOperator.LE_OP:
            result = (self.expr1.evaluate() <= self.expr2.evaluate())
        elif self.op == RelationalOperator.GT_OP:
            result = (self.expr1.evaluate() > self.expr2.evaluate())
        elif self.op == RelationalOperator.GE_OP:
            result = (self.expr1.evaluate() >= self.expr2.evaluate())
        else:
            raise Exception("invalid relational operator argument in Boolean Expression")

        return result
