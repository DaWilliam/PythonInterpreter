from Statement import Statement
from BooleanExpression import BooleanExpression
from Block import Block


class IfStatement(Statement):
    expr = None
    blk1 = None
    blk2 = None

    def __init__(self, expr, blk1, blk2):
        if expr is None:
            raise Exception("null boolean expression argument")
        if blk1 is None or blk2 is None:
            raise Exception("null block argument")
        self.expr = expr
        self.blk1 = blk1
        self.blk2 = blk2

    def execute(self):
        if self.expr.evaluate():
            self.blk1.execute()
        else:
            self.blk2.execute()
