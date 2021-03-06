from Statement import Statement


class WhileStatement(Statement):
    expr = None
    blk = None

    def __init__(self, expr, blk):
        if expr is None:
            raise Exception("null boolean expression argument")
        if blk is None:
            raise Exception("null block argument")

        self.expr = expr
        self.blk = blk

    def execute(self):
        while self.expr.evaluate():
            self.blk.execute()
