from RepeatStatement import RepeatStatement
from TokenType import TokenType
from LexicalAnalyzer import LexicalAnalyzer
from Id import Id
from Program import Program
from Block import Block
from LiteralInteger import LiteralInteger
from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression
from ArithmeticOperator import ArithmeticOperator
from PrintStatement import PrintStatement
from IfStatement import IfStatement
from RelationalOperator import RelationalOperator
from BooleanExpression import BooleanExpression
from WhileStatement import WhileStatement
from ForStatement import ForStatement


class Parser:
    lex = None

    def __init__(self, fileName):
        self.lex = LexicalAnalyzer(fileName)

    def parse(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.FUNCTION_TOK)
        functionName = self.getId()
        tok = self.getNextToken()
        self.match(tok, TokenType.LEFT_PAREN_TOK)
        tok = self.getNextToken()
        self.match(tok, TokenType.RIGHT_PAREN_TOK)
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        tok = self.getNextToken()
        if tok.getTokType() != TokenType.EOS_TOK:
            raise Exception("garbage at end of file")
        return Program(blk)

    def getBlock(self):
        blk = Block()
        tok = self.getLookaheadToken()
        while self.isValidStartOfStatement(tok):
            stmt = self.getStatement()
            blk.add(stmt)
            tok = self.getLookaheadToken()
        return blk

    def getStatement(self):
        stmt = None
        tok = self.getLookaheadToken()

        if tok.getTokType() == TokenType.IF_TOK:
            stmt = self.getIfStatement()
        elif tok.getTokType() == TokenType.WHILE_TOK:
            stmt = self.getWhileStatement()
        elif tok.getTokType() == TokenType.PRINT_TOK:
            stmt = self.getPrintStatement()
        elif tok.getTokType() == TokenType.REPEAT_TOK:
            stmt = self.getRepeatStatement()
        elif tok.getTokType() == TokenType.ID_TOK:
            stmt = self.getAssignmentStatement()
        elif tok.getTokType() == TokenType.FOR_TOK:
            stmt = self.getForStatement()
        else:
            raise Exception("invalid statement at row " + tok.getRowNumber() +
                            " and column " + tok.getColumnNumber())
        return stmt

    def getAssignmentStatement(self):
        var = self.getId()
        tok = self.getNextToken()
        self.match(tok, TokenType.ASSIGN_TOK)
        expr = self.getArithmeticExpression()
        return AssignmentStatement(var, expr)

    def getRepeatStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.REPEAT_TOK)
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, TokenType.UNTIL_TOK)
        expr = self.getBooleanExpression()
        return RepeatStatement(blk, expr)

    def getPrintStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.PRINT_TOK)
        tok = self.getNextToken()
        self.match(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.getArithmeticExpression()
        tok = self.getNextToken()
        self.match(tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expr)

    def getWhileStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.getBooleanExpression()
        tok = self.getNextToken()
        self.match(tok, TokenType.DO_TOK)
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        return WhileStatement(expr, blk)

    def getIfStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.IF_TOK)
        expr = self.getBooleanExpression()
        tok = self.getNextToken()
        self.match(tok, TokenType.THEN_TOK)
        blk1 = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, TokenType.ELSE_TOK)
        blk2 = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        return IfStatement(expr, blk1, blk2)

    def isValidStartOfStatement(self, tok):
        assert tok is not None
        return tok.getTokType() == TokenType.ID_TOK or tok.getTokType() == TokenType.IF_TOK or tok.getTokType() == TokenType.WHILE_TOK or tok.getTokType() == TokenType.PRINT_TOK or tok.getTokType() == TokenType.REPEAT_TOK or tok.getTokType() == TokenType.FOR_TOK

    def getArithmeticExpression(self):
        expr = None
        tok = self.getLookaheadToken()
        if tok.getTokType() == TokenType.ID_TOK:
            expr = self.getId()
        elif tok.getTokType() == TokenType.LITERAL_INTEGER_TOK:
            expr = self.getLiteralInteger()
        else:
            expr = self.getBinaryExpression()
        return expr

    def getBinaryExpression(self):
        op = self.getArithmeticOperator()
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        return BinaryExpression(op, expr1, expr2)

    def getArithmeticOperator(self):
        op = None
        tok = self.getNextToken()
        if tok.getTokType() == TokenType.ADD_TOK:
            op = ArithmeticOperator.ADD_OP
        elif tok.getTokType() == TokenType.SUB_TOK:
            op = ArithmeticOperator.SUB_OP
        elif tok.getTokType() == TokenType.MUL_TOK:
            op = ArithmeticOperator.MUL_OP
        elif tok.getTokType() == TokenType.DIV_TOK:
            op = ArithmeticOperator.DIV_OP
        else:
            raise Exception(
                "arithmetic operator expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())
        return op

    def getLiteralInteger(self):
        tok = self.getNextToken()
        if tok.getTokType() != TokenType.LITERAL_INTEGER_TOK:
            raise Exception(
                "literal integer expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())
        value = int(tok.getLexeme())
        return LiteralInteger(value)

    def getId(self):
        tok = self.getNextToken()
        if tok.getTokType() != TokenType.ID_TOK:
            raise Exception(
                "identifier expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber());
        return Id(tok.getLexeme()[0])

    def getBooleanExpression(self):
        op = self.getRelationalOperator()
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        return BooleanExpression(op, expr1, expr2)

    def getRelationalOperator(self):
        op = None
        tok = self.getNextToken()
        if tok.getTokType() == TokenType.EQ_TOK:
            op = RelationalOperator.EQ_OP
        elif (tok.getTokType() == TokenType.NE_TOK):
            op = RelationalOperator.NE_OP
        elif (tok.getTokType() == TokenType.GT_TOK):
            op = RelationalOperator.GT_OP
        elif (tok.getTokType() == TokenType.GE_TOK):
            op = RelationalOperator.GE_OP
        elif (tok.getTokType() == TokenType.LT_TOK):
            op = RelationalOperator.LT_OP
        elif (tok.getTokType() == TokenType.LE_TOK):
            op = RelationalOperator.LE_OP
        else:
            raise Exception(
                "relational operator expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())

        return op

    def match(self, tok, tokType):
        assert tok != None
        assert tokType != None
        if tok.getTokType() != tokType:
            raise Exception(str(tokType.name) + " expected at row " + str(tok.getRowNumber()) + " and column " + str(
                tok.getColumnNumber()))

    def getLookaheadToken(self):
        tok = None
        try:
            tok = self.lex.getLookaheadToken()
        except:
            raise Exception("no more tokens")
        return tok

    def getNextToken(self):
        tok = None
        try:
            tok = self.lex.getNextToken()
        except:
            raise Exception("no more tokens")
        return tok

    def getForStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.FOR_TOK)
        assign = self.getAssignmentStatement()
        assign.execute()
        id = assign.getId()
        tok = self.getNextToken()
        self.match(tok, TokenType.BETWEEN_TOK)
        end = self.getArithmeticExpression()
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        return ForStatement(id, blk, end)
