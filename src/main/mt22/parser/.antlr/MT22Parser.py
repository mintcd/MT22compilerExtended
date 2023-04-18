# Generated from c:\Projects\extened-PPL-master\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\5")
        buf.write("\5*\n\5\3\5\3\5\3\5\5\5/\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\5\n@\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13G\n\13\3\f\3\f\3\r\3\r\3\r\5\rN\n")
        buf.write("\r\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2")
        buf.write("\4\3\2\5\6\3\2\7\t\2J\2\32\3\2\2\2\4!\3\2\2\2\6#\3\2\2")
        buf.write("\2\b.\3\2\2\2\n\60\3\2\2\2\f\62\3\2\2\2\16\66\3\2\2\2")
        buf.write("\20;\3\2\2\2\22?\3\2\2\2\24F\3\2\2\2\26H\3\2\2\2\30J\3")
        buf.write("\2\2\2\32\33\5\4\3\2\33\34\7\3\2\2\34\35\7\13\2\2\35\36")
        buf.write("\7\f\2\2\36\37\5\6\4\2\37 \7\2\2\3 \3\3\2\2\2!\"\t\2\2")
        buf.write("\2\"\5\3\2\2\2#$\7\r\2\2$%\5\b\5\2%&\7\16\2\2&\7\3\2\2")
        buf.write("\2\'*\5\n\6\2(*\5\f\7\2)\'\3\2\2\2)(\3\2\2\2*+\3\2\2\2")
        buf.write("+,\5\b\5\2,/\3\2\2\2-/\3\2\2\2.)\3\2\2\2.-\3\2\2\2/\t")
        buf.write("\3\2\2\2\60\61\5\16\b\2\61\13\3\2\2\2\62\63\5\4\3\2\63")
        buf.write("\64\7\7\2\2\64\65\7\17\2\2\65\r\3\2\2\2\66\67\5\20\t\2")
        buf.write("\678\7\4\2\289\5\22\n\29:\7\17\2\2:\17\3\2\2\2;<\7\7\2")
        buf.write("\2<\21\3\2\2\2=@\5\24\13\2>@\7\7\2\2?=\3\2\2\2?>\3\2\2")
        buf.write("\2@\23\3\2\2\2AB\5\26\f\2BC\7\n\2\2CD\5\24\13\2DG\3\2")
        buf.write("\2\2EG\5\26\f\2FA\3\2\2\2FE\3\2\2\2G\25\3\2\2\2HI\t\3")
        buf.write("\2\2I\27\3\2\2\2JK\7\7\2\2KM\7\13\2\2LN\5\24\13\2ML\3")
        buf.write("\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\f\2\2P\31\3\2\2\2\7).?")
        buf.write("FM")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'='", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'('", "')'", "'{'", 
                     "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ASSIGN", "INTTYPE", "VOIDTYPE", 
                      "ID", "INTLIT", "FLOATLIT", "ADD", "LB", "RB", "LP", 
                      "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_blockstmt = 2
    RULE_stmtlist = 3
    RULE_stmt = 4
    RULE_vardecl = 5
    RULE_assignstmt = 6
    RULE_lhs = 7
    RULE_rhs = 8
    RULE_exp = 9
    RULE_exp1 = 10
    RULE_funcall = 11

    ruleNames =  [ "program", "mptype", "blockstmt", "stmtlist", "stmt", 
                   "vardecl", "assignstmt", "lhs", "rhs", "exp", "exp1", 
                   "funcall" ]

    EOF = Token.EOF
    T__0=1
    ASSIGN=2
    INTTYPE=3
    VOIDTYPE=4
    ID=5
    INTLIT=6
    FLOATLIT=7
    ADD=8
    LB=9
    RB=10
    LP=11
    RP=12
    SEMI=13
    WS=14
    ERROR_CHAR=15
    UNCLOSE_STRING=16
    ILLEGAL_ESCAPE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MT22Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.mptype()
            self.state = 25
            self.match(MT22Parser.T__0)
            self.state = 26
            self.match(MT22Parser.LB)
            self.state = 27
            self.match(MT22Parser.RB)
            self.state = 28
            self.blockstmt()
            self.state = 29
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MT22Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MT22Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_mptype




    def mptype(self):

        localctx = MT22Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            _la = self._input.LA(1)
            if not(_la==MT22Parser.INTTYPE or _la==MT22Parser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MT22Parser.LP)
            self.state = 34
            self.stmtlist()
            self.state = 35
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtlist




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmtlist)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTTYPE, MT22Parser.VOIDTYPE, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MT22Parser.ID]:
                    self.state = 37
                    self.stmt()
                    pass
                elif token in [MT22Parser.INTTYPE, MT22Parser.VOIDTYPE]:
                    self.state = 38
                    self.vardecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 41
                self.stmtlist()
                pass
            elif token in [MT22Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.assignstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MT22Parser.MptypeContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.mptype()
            self.state = 49
            self.match(MT22Parser.ID)
            self.state = 50
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def rhs(self):
            return self.getTypedRuleContext(MT22Parser.RhsContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.lhs()
            self.state = 53
            self.match(MT22Parser.ASSIGN)
            self.state = 54
            self.rhs()
            self.state = 55
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_rhs




    def rhs(self):

        localctx = MT22Parser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rhs)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MT22Parser.Exp1Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp




    def exp(self):

        localctx = MT22Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.exp1()
                self.state = 64
                self.match(MT22Parser.ADD)
                self.state = 65
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp1




    def exp1(self):

        localctx = MT22Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcall




    def funcall(self):

        localctx = MT22Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MT22Parser.ID)
            self.state = 73
            self.match(MT22Parser.LB)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT))) != 0):
                self.state = 74
                self.exp()


            self.state = 77
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





