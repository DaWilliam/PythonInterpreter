from ArithmeticExpression import ArithmeticExpression
from Memory import Memory

class Id(ArithmeticExpression):

    ch = None

    def __init__(self, ch):
        if not ch.isalpha():
            raise  Exception ("invalid identifier argument.")
        self.ch = ch

    def getChar(self):
        return self.ch

    def evaluate(self):
        return Memory.fetch(self.ch)
