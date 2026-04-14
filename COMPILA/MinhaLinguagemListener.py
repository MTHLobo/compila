# Generated from MinhaLinguagem.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MinhaLinguagemParser import MinhaLinguagemParser
else:
    from MinhaLinguagemParser import MinhaLinguagemParser

# This class defines a complete listener for a parse tree produced by MinhaLinguagemParser.
class MinhaLinguagemListener(ParseTreeListener):

    # Enter a parse tree produced by MinhaLinguagemParser#programa.
    def enterPrograma(self, ctx:MinhaLinguagemParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#programa.
    def exitPrograma(self, ctx:MinhaLinguagemParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#pacote.
    def enterPacote(self, ctx:MinhaLinguagemParser.PacoteContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#pacote.
    def exitPacote(self, ctx:MinhaLinguagemParser.PacoteContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#declaracaoFunc.
    def enterDeclaracaoFunc(self, ctx:MinhaLinguagemParser.DeclaracaoFuncContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#declaracaoFunc.
    def exitDeclaracaoFunc(self, ctx:MinhaLinguagemParser.DeclaracaoFuncContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#bloco.
    def enterBloco(self, ctx:MinhaLinguagemParser.BlocoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#bloco.
    def exitBloco(self, ctx:MinhaLinguagemParser.BlocoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#comando.
    def enterComando(self, ctx:MinhaLinguagemParser.ComandoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#comando.
    def exitComando(self, ctx:MinhaLinguagemParser.ComandoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#variavelDecl.
    def enterVariavelDecl(self, ctx:MinhaLinguagemParser.VariavelDeclContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#variavelDecl.
    def exitVariavelDecl(self, ctx:MinhaLinguagemParser.VariavelDeclContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#atribuicao.
    def enterAtribuicao(self, ctx:MinhaLinguagemParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#atribuicao.
    def exitAtribuicao(self, ctx:MinhaLinguagemParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#cmdLeia.
    def enterCmdLeia(self, ctx:MinhaLinguagemParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#cmdLeia.
    def exitCmdLeia(self, ctx:MinhaLinguagemParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:MinhaLinguagemParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:MinhaLinguagemParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#cmdSe.
    def enterCmdSe(self, ctx:MinhaLinguagemParser.CmdSeContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#cmdSe.
    def exitCmdSe(self, ctx:MinhaLinguagemParser.CmdSeContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:MinhaLinguagemParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:MinhaLinguagemParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprNao.
    def enterExprNao(self, ctx:MinhaLinguagemParser.ExprNaoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprNao.
    def exitExprNao(self, ctx:MinhaLinguagemParser.ExprNaoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprString.
    def enterExprString(self, ctx:MinhaLinguagemParser.ExprStringContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprString.
    def exitExprString(self, ctx:MinhaLinguagemParser.ExprStringContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprNumero.
    def enterExprNumero(self, ctx:MinhaLinguagemParser.ExprNumeroContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprNumero.
    def exitExprNumero(self, ctx:MinhaLinguagemParser.ExprNumeroContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprMultDiv.
    def enterExprMultDiv(self, ctx:MinhaLinguagemParser.ExprMultDivContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprMultDiv.
    def exitExprMultDiv(self, ctx:MinhaLinguagemParser.ExprMultDivContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprIgual.
    def enterExprIgual(self, ctx:MinhaLinguagemParser.ExprIgualContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprIgual.
    def exitExprIgual(self, ctx:MinhaLinguagemParser.ExprIgualContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprParenteses.
    def enterExprParenteses(self, ctx:MinhaLinguagemParser.ExprParentesesContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprParenteses.
    def exitExprParenteses(self, ctx:MinhaLinguagemParser.ExprParentesesContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprId.
    def enterExprId(self, ctx:MinhaLinguagemParser.ExprIdContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprId.
    def exitExprId(self, ctx:MinhaLinguagemParser.ExprIdContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprLogica.
    def enterExprLogica(self, ctx:MinhaLinguagemParser.ExprLogicaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprLogica.
    def exitExprLogica(self, ctx:MinhaLinguagemParser.ExprLogicaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprSomaSub.
    def enterExprSomaSub(self, ctx:MinhaLinguagemParser.ExprSomaSubContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprSomaSub.
    def exitExprSomaSub(self, ctx:MinhaLinguagemParser.ExprSomaSubContext):
        pass



del MinhaLinguagemParser