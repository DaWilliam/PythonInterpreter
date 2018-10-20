from TokenType import TokenType
from Token import Token

class LexicalAnalyzer:

    tokenList = []

    def __init__(self, fileName): #(self, fileName):
        if fileName == None:
            raise Exception("null file name argument")
        self.tokenList = []
        input = open(fileName, 'r')
        lineNumber = 0
        for line in input:
            lineNumber = lineNumber + 1
            self.processLine(line, lineNumber)
        input.close()
        self.tokenList.append(Token(TokenType.EOS_TOK, "EOS", lineNumber, 1))

    def processLine(self, line, lineNumber):
        if line == None:
            raise Exception("null line argument")
        if lineNumber <= 0:
            raise Exception("invalid line number argument")
        index = self.skipWhiteSpace(line, 0)

        while index < len(line):
            lexeme = self.getLexeme(line, index)

            tokType = self.getTokenType(lexeme, lineNumber, index + 1)
            self.tokenList.append(Token(tokType, lexeme, lineNumber, index + 1))
            index += len(lexeme)
            index = self.skipWhiteSpace(line, index)

    def getTokenType(self, lexeme, rowNumber, columnNumber):
        if lexeme == None or len(lexeme) == 0:
            raise Exception("invalid string argument")
        tokType = TokenType.EOS_TOK

        if lexeme[0].isdigit():
            if self.allDigits(lexeme):
                tokType = TokenType.LITERAL_INTEGER_TOK
            else:
                raise Exception("literal integer expecated " + " at row " + rowNumber  + " and column " + columnNumber)
        elif lexeme[0].isalpha():
            if len(lexeme) == 1:
                tokType = TokenType.ID_TOK
            elif lexeme == "if":
                tokType = TokenType.IF_TOK
            elif lexeme == "function":
                tokType = TokenType.FUNCTION_TOK
            elif lexeme == "then":
                tokType = TokenType.THEN_TOK
            elif lexeme == "end":
                tokType = TokenType.END_TOK
            elif lexeme == "else":
                tokType = TokenType.ELSE_TOK
            elif lexeme == "while":
                tokType = TokenType.WHILE_TOK
            elif lexeme == "do":
                tokType = TokenType.DO_TOK
            elif lexeme == "print":
                tokType = TokenType.PRINT_TOK
            elif lexeme == "repeat":
                tokType = TokenType.REPEAT_TOK
            elif lexeme == "until":
                tokType = TokenType.UNTIL_TOK
            elif lexeme == "for":
                tokType = TokenType.FOR_TOK
            else:
                raise Exception("invalid lexeme " + " at row " + rowNumber  + " and column " + columnNumber)

        elif lexeme == "(":
            tokType = TokenType.LEFT_PAREN_TOK
        elif lexeme == ")":
            tokType = TokenType.RIGHT_PAREN_TOK
        elif lexeme == ">=":
            tokType = TokenType.GE_TOK
        elif lexeme == ">":
            tokType = TokenType.GT_TOK
        elif lexeme == "<=":
            tokType = TokenType.LE_TOK
        elif lexeme == "<":
            tokType = TokenType.LT_TOK
        elif lexeme == "==":
            tokType = TokenType.EQ_TOK
        elif lexeme == "!=":
            tokType = TokenType.NE_TOK
        elif lexeme == "+":
            tokType = TokenType.ADD_TOK
        elif lexeme == "-":
            tokType = TokenType.SUB_TOK
        elif lexeme == "*":
            tokType = TokenType.MUL_TOK
        elif lexeme == "/":
            tokType = TokenType.DIV_TOK
        elif lexeme == "=":
            tokType = TokenType.ASSIGN_TOK
        elif lexeme == ":":
            tokType = TokenType.BETWEEN_TOK
        else:
            raise Exception("invalid lexeme " + " at row " + rowNumber  + " and column " + columnNumber)

        return tokType

    def allDigits(self, lexeme):
        if lexeme == None:
            raise Exception("null string argument")
        i = 0
        while i < len(lexeme) and lexeme[i].isdigit():
            i = i + 1
        return (i == len(lexeme))

    def getLexeme(self, line, index):
        if line == None:
            raise Exception("null string argument")
        if index < 0:
            raise Exception("incalid index argument")
        i = index
        while i < len(line) and not line[i].isspace():
            i = i + 1

        if -(len(line) - i) == 0:
            return line[index : len(line)]
        else:
            return line[index : -(len(line) - i)]


    def skipWhiteSpace(self, line, index):
        while index < len(line) and line[index].isspace():
            index = index + 1
        return index

    def getLookaheadToken(self):
        if not self.tokenList:
            raise Exception ("no more tokens")
        return self.tokenList[0]

    def getNextToken(self):
        if not self.tokenList:
            raise Exception ("no more tokens")
        return self.tokenList.pop(0)



