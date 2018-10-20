from Statement import Statement

class RepeatStatement(Statement):

    blk = None
    expr = None

    def __init__(self, blk, expr):
        if blk == None:
            raise Exception("null block argument")
        if expr == None:
            raise Exception ("null boolean expression argument")
        self.blk = blk
        self.expr = expr

    def execute(self):
        blk.execute()
        while not expr.evaluate():
            blk.execute