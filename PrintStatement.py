from Statement import Statement

class PrintStatement(Statement):

    expr = None

    def __init__(self, expr):
        if expr == None:
            raise Exception("null arithmetic expression argument")
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())