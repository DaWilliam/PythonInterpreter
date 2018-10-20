from Statement import Statement
from ArithmeticExpression import ArithmeticExpression
from Id import Id
from Memory import Memory

class AssignmentStatement (Statement):

    var = None
    expr = None

    def __init__(self, var, expr):
        if (var == None):
            raise Exception ("Null Id Argument")
        if (expr == None):
            raise Exception ("Null ArithmeticExpression Expression")
        self.var = var
        self.expr = expr

    def execute(self):
        Memory.store(self.var.getChar(), self.expr.evaluate())

    def getId(self):
        return self.var
