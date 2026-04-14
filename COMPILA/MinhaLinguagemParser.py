# Generated from MinhaLinguagem.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,4,0,27,8,0,
        11,0,12,0,28,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        5,3,44,8,3,10,3,12,3,47,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        57,8,4,1,5,1,5,1,5,1,5,1,5,3,5,64,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,86,8,9,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,103,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,5,11,117,8,11,10,11,12,11,120,9,11,1,11,0,1,
        22,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,1,0,18,19,1,0,20,21,1,0,
        23,24,126,0,24,1,0,0,0,2,32,1,0,0,0,4,35,1,0,0,0,6,41,1,0,0,0,8,
        56,1,0,0,0,10,58,1,0,0,0,12,65,1,0,0,0,14,69,1,0,0,0,16,74,1,0,0,
        0,18,79,1,0,0,0,20,87,1,0,0,0,22,102,1,0,0,0,24,26,3,2,1,0,25,27,
        3,4,2,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,
        29,30,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,34,5,25,
        0,0,34,3,1,0,0,0,35,36,5,2,0,0,36,37,5,25,0,0,37,38,5,3,0,0,38,39,
        5,4,0,0,39,40,3,6,3,0,40,5,1,0,0,0,41,45,5,5,0,0,42,44,3,8,4,0,43,
        42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,
        0,47,45,1,0,0,0,48,49,5,6,0,0,49,7,1,0,0,0,50,57,3,10,5,0,51,57,
        3,12,6,0,52,57,3,14,7,0,53,57,3,16,8,0,54,57,3,18,9,0,55,57,3,20,
        10,0,56,50,1,0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,
        54,1,0,0,0,56,55,1,0,0,0,57,9,1,0,0,0,58,59,5,7,0,0,59,60,5,25,0,
        0,60,63,5,16,0,0,61,62,5,8,0,0,62,64,3,22,11,0,63,61,1,0,0,0,63,
        64,1,0,0,0,64,11,1,0,0,0,65,66,5,25,0,0,66,67,5,8,0,0,67,68,3,22,
        11,0,68,13,1,0,0,0,69,70,5,9,0,0,70,71,5,3,0,0,71,72,5,25,0,0,72,
        73,5,4,0,0,73,15,1,0,0,0,74,75,5,10,0,0,75,76,5,3,0,0,76,77,3,22,
        11,0,77,78,5,4,0,0,78,17,1,0,0,0,79,80,5,11,0,0,80,81,3,22,11,0,
        81,82,5,12,0,0,82,85,3,6,3,0,83,84,5,13,0,0,84,86,3,6,3,0,85,83,
        1,0,0,0,85,86,1,0,0,0,86,19,1,0,0,0,87,88,5,14,0,0,88,89,3,22,11,
        0,89,90,5,15,0,0,90,91,3,6,3,0,91,21,1,0,0,0,92,93,6,11,-1,0,93,
        94,5,3,0,0,94,95,3,22,11,0,95,96,5,4,0,0,96,103,1,0,0,0,97,98,5,
        17,0,0,98,103,3,22,11,8,99,103,5,25,0,0,100,103,5,26,0,0,101,103,
        5,27,0,0,102,92,1,0,0,0,102,97,1,0,0,0,102,99,1,0,0,0,102,100,1,
        0,0,0,102,101,1,0,0,0,103,118,1,0,0,0,104,105,10,7,0,0,105,106,7,
        0,0,0,106,117,3,22,11,8,107,108,10,6,0,0,108,109,7,1,0,0,109,117,
        3,22,11,7,110,111,10,5,0,0,111,112,5,22,0,0,112,117,3,22,11,6,113,
        114,10,4,0,0,114,115,7,2,0,0,115,117,3,22,11,5,116,104,1,0,0,0,116,
        107,1,0,0,0,116,110,1,0,0,0,116,113,1,0,0,0,117,120,1,0,0,0,118,
        116,1,0,0,0,118,119,1,0,0,0,119,23,1,0,0,0,120,118,1,0,0,0,8,28,
        45,56,63,85,102,116,118
    ]

class MinhaLinguagemParser ( Parser ):

    grammarFileName = "MinhaLinguagem.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pacote'", "'func'", "'('", "')'", "'{'", 
                     "'}'", "'var'", "'='", "'leia'", "'escreva'", "'se'", 
                     "'entao'", "'senao'", "'enquanto'", "'faca'", "<INVALID>", 
                     "'!'", "'*'", "'/'", "'+'", "'-'", "'=='", "'&&'", 
                     "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TIPO", "NAO", "MULT", "DIV", "SOMA", "SUB", "IGUAL", 
                      "E_LOGICO", "OU_LOGICO", "ID", "NUMERO", "STRING_VAL", 
                      "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_pacote = 1
    RULE_declaracaoFunc = 2
    RULE_bloco = 3
    RULE_comando = 4
    RULE_variavelDecl = 5
    RULE_atribuicao = 6
    RULE_cmdLeia = 7
    RULE_cmdEscreva = 8
    RULE_cmdSe = 9
    RULE_cmdEnquanto = 10
    RULE_expressao = 11

    ruleNames =  [ "programa", "pacote", "declaracaoFunc", "bloco", "comando", 
                   "variavelDecl", "atribuicao", "cmdLeia", "cmdEscreva", 
                   "cmdSe", "cmdEnquanto", "expressao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    TIPO=16
    NAO=17
    MULT=18
    DIV=19
    SOMA=20
    SUB=21
    IGUAL=22
    E_LOGICO=23
    OU_LOGICO=24
    ID=25
    NUMERO=26
    STRING_VAL=27
    WS=28
    COMENTARIO=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pacote(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.PacoteContext,0)


        def EOF(self):
            return self.getToken(MinhaLinguagemParser.EOF, 0)

        def declaracaoFunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.DeclaracaoFuncContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.DeclaracaoFuncContext,i)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = MinhaLinguagemParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.pacote()
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.declaracaoFunc()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 30
            self.match(MinhaLinguagemParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PacoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MinhaLinguagemParser.ID, 0)

        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_pacote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPacote" ):
                listener.enterPacote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPacote" ):
                listener.exitPacote(self)




    def pacote(self):

        localctx = MinhaLinguagemParser.PacoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pacote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MinhaLinguagemParser.T__0)
            self.state = 33
            self.match(MinhaLinguagemParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MinhaLinguagemParser.ID, 0)

        def bloco(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.BlocoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_declaracaoFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoFunc" ):
                listener.enterDeclaracaoFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoFunc" ):
                listener.exitDeclaracaoFunc(self)




    def declaracaoFunc(self):

        localctx = MinhaLinguagemParser.DeclaracaoFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracaoFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MinhaLinguagemParser.T__1)
            self.state = 36
            self.match(MinhaLinguagemParser.ID)
            self.state = 37
            self.match(MinhaLinguagemParser.T__2)
            self.state = 38
            self.match(MinhaLinguagemParser.T__3)
            self.state = 39
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ComandoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ComandoContext,i)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = MinhaLinguagemParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(MinhaLinguagemParser.T__4)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33574528) != 0):
                self.state = 42
                self.comando()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(MinhaLinguagemParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variavelDecl(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.VariavelDeclContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.AtribuicaoContext,0)


        def cmdLeia(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.CmdLeiaContext,0)


        def cmdEscreva(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.CmdEscrevaContext,0)


        def cmdSe(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.CmdSeContext,0)


        def cmdEnquanto(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.CmdEnquantoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = MinhaLinguagemParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comando)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.variavelDecl()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.atribuicao()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.cmdLeia()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.cmdEscreva()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.cmdSe()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.cmdEnquanto()
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


    class VariavelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MinhaLinguagemParser.ID, 0)

        def TIPO(self):
            return self.getToken(MinhaLinguagemParser.TIPO, 0)

        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_variavelDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavelDecl" ):
                listener.enterVariavelDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavelDecl" ):
                listener.exitVariavelDecl(self)




    def variavelDecl(self):

        localctx = MinhaLinguagemParser.VariavelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variavelDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MinhaLinguagemParser.T__6)
            self.state = 59
            self.match(MinhaLinguagemParser.ID)
            self.state = 60
            self.match(MinhaLinguagemParser.TIPO)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 61
                self.match(MinhaLinguagemParser.T__7)
                self.state = 62
                self.expressao(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MinhaLinguagemParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = MinhaLinguagemParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MinhaLinguagemParser.ID)
            self.state = 66
            self.match(MinhaLinguagemParser.T__7)
            self.state = 67
            self.expressao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdLeiaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MinhaLinguagemParser.ID, 0)

        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_cmdLeia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdLeia" ):
                listener.enterCmdLeia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdLeia" ):
                listener.exitCmdLeia(self)




    def cmdLeia(self):

        localctx = MinhaLinguagemParser.CmdLeiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdLeia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MinhaLinguagemParser.T__8)
            self.state = 70
            self.match(MinhaLinguagemParser.T__2)
            self.state = 71
            self.match(MinhaLinguagemParser.ID)
            self.state = 72
            self.match(MinhaLinguagemParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdEscrevaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_cmdEscreva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdEscreva" ):
                listener.enterCmdEscreva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdEscreva" ):
                listener.exitCmdEscreva(self)




    def cmdEscreva(self):

        localctx = MinhaLinguagemParser.CmdEscrevaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdEscreva)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(MinhaLinguagemParser.T__9)
            self.state = 75
            self.match(MinhaLinguagemParser.T__2)
            self.state = 76
            self.expressao(0)
            self.state = 77
            self.match(MinhaLinguagemParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdSeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.BlocoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.BlocoContext,i)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_cmdSe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdSe" ):
                listener.enterCmdSe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdSe" ):
                listener.exitCmdSe(self)




    def cmdSe(self):

        localctx = MinhaLinguagemParser.CmdSeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdSe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MinhaLinguagemParser.T__10)
            self.state = 80
            self.expressao(0)
            self.state = 81
            self.match(MinhaLinguagemParser.T__11)
            self.state = 82
            self.bloco()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 83
                self.match(MinhaLinguagemParser.T__12)
                self.state = 84
                self.bloco()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdEnquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def bloco(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.BlocoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_cmdEnquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdEnquanto" ):
                listener.enterCmdEnquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdEnquanto" ):
                listener.exitCmdEnquanto(self)




    def cmdEnquanto(self):

        localctx = MinhaLinguagemParser.CmdEnquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdEnquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MinhaLinguagemParser.T__13)
            self.state = 88
            self.expressao(0)
            self.state = 89
            self.match(MinhaLinguagemParser.T__14)
            self.state = 90
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_expressao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprNaoContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAO(self):
            return self.getToken(MinhaLinguagemParser.NAO, 0)
        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNao" ):
                listener.enterExprNao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNao" ):
                listener.exitExprNao(self)


    class ExprStringContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_VAL(self):
            return self.getToken(MinhaLinguagemParser.STRING_VAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprString" ):
                listener.enterExprString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprString" ):
                listener.exitExprString(self)


    class ExprNumeroContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(MinhaLinguagemParser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNumero" ):
                listener.enterExprNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNumero" ):
                listener.exitExprNumero(self)


    class ExprMultDivContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,i)

        def MULT(self):
            return self.getToken(MinhaLinguagemParser.MULT, 0)
        def DIV(self):
            return self.getToken(MinhaLinguagemParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultDiv" ):
                listener.enterExprMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultDiv" ):
                listener.exitExprMultDiv(self)


    class ExprIgualContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,i)

        def IGUAL(self):
            return self.getToken(MinhaLinguagemParser.IGUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprIgual" ):
                listener.enterExprIgual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprIgual" ):
                listener.exitExprIgual(self)


    class ExprParentesesContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParenteses" ):
                listener.enterExprParenteses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParenteses" ):
                listener.exitExprParenteses(self)


    class ExprIdContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MinhaLinguagemParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprId" ):
                listener.enterExprId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprId" ):
                listener.exitExprId(self)


    class ExprLogicaContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,i)

        def E_LOGICO(self):
            return self.getToken(MinhaLinguagemParser.E_LOGICO, 0)
        def OU_LOGICO(self):
            return self.getToken(MinhaLinguagemParser.OU_LOGICO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogica" ):
                listener.enterExprLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogica" ):
                listener.exitExprLogica(self)


    class ExprSomaSubContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExpressaoContext,i)

        def SOMA(self):
            return self.getToken(MinhaLinguagemParser.SOMA, 0)
        def SUB(self):
            return self.getToken(MinhaLinguagemParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSomaSub" ):
                listener.enterExprSomaSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSomaSub" ):
                listener.exitExprSomaSub(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MinhaLinguagemParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = MinhaLinguagemParser.ExprParentesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 93
                self.match(MinhaLinguagemParser.T__2)
                self.state = 94
                self.expressao(0)
                self.state = 95
                self.match(MinhaLinguagemParser.T__3)
                pass
            elif token in [17]:
                localctx = MinhaLinguagemParser.ExprNaoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(MinhaLinguagemParser.NAO)
                self.state = 98
                self.expressao(8)
                pass
            elif token in [25]:
                localctx = MinhaLinguagemParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(MinhaLinguagemParser.ID)
                pass
            elif token in [26]:
                localctx = MinhaLinguagemParser.ExprNumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                self.match(MinhaLinguagemParser.NUMERO)
                pass
            elif token in [27]:
                localctx = MinhaLinguagemParser.ExprStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(MinhaLinguagemParser.STRING_VAL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MinhaLinguagemParser.ExprMultDivContext(self, MinhaLinguagemParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 104
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 105
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expressao(8)
                        pass

                    elif la_ == 2:
                        localctx = MinhaLinguagemParser.ExprSomaSubContext(self, MinhaLinguagemParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 107
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 108
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expressao(7)
                        pass

                    elif la_ == 3:
                        localctx = MinhaLinguagemParser.ExprIgualContext(self, MinhaLinguagemParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 110
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 111
                        self.match(MinhaLinguagemParser.IGUAL)
                        self.state = 112
                        self.expressao(6)
                        pass

                    elif la_ == 4:
                        localctx = MinhaLinguagemParser.ExprLogicaContext(self, MinhaLinguagemParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 113
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 114
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expressao(5)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




