from Statement import Statement
from Memory import Memory

class ForStatement(Statement):

    var = None
    blk = None
    end = None

    def __init__(self, var, blk, end):
        if var == None:
            raise Exception("null arithmetic expression argument")
        if blk == None:
            raise Exception("null block argument")
        if end == None:
            raise Exception("null arithmetic argument")

        self.var = var
        self.blk = blk
        self.end = end

    def execute(self):
        i = self.var.evaluate()
        e = self.end.evaluate()
        while i <= e:
            Memory.store(self.var.getChar(), i)
            self.blk.execute()
            i = i + 1