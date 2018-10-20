from TokenType import TokenType


class Token:
    tokType = None
    lexeme = "Didn't Define it Yet"
    rowNumber = -1
    columnNumber = -1

    def __init__(self, tokType, lexeme, rowNumber, columnNumber):
        if tokType is None:
            raise Exception("null TokenType argument")
        if lexeme is None or len(lexeme) == 0:
            raise Exception("invalid lexeme argument")
        if rowNumber <= 0:
            raise Exception("invalid row number argument")
        if columnNumber <= 0:
            raise Exception("invlid column number argment")

        self.tokType = tokType
        self.lexeme = lexeme
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber

    def getTokType(self):
        return self.tokType

    def getLexeme(self):
        return self.lexeme

    def getRowNumber(self):
        return self.rowNumber

    def getColumnNumber(self):
        return self.columnNumber
