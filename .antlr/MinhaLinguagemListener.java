// Generated from c:/Users/ABA/Documents/COMPILA/MinhaLinguagem.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MinhaLinguagemParser}.
 */
public interface MinhaLinguagemListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(MinhaLinguagemParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(MinhaLinguagemParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#pacote}.
	 * @param ctx the parse tree
	 */
	void enterPacote(MinhaLinguagemParser.PacoteContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#pacote}.
	 * @param ctx the parse tree
	 */
	void exitPacote(MinhaLinguagemParser.PacoteContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#declaracaoFunc}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracaoFunc(MinhaLinguagemParser.DeclaracaoFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#declaracaoFunc}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracaoFunc(MinhaLinguagemParser.DeclaracaoFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#bloco}.
	 * @param ctx the parse tree
	 */
	void enterBloco(MinhaLinguagemParser.BlocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#bloco}.
	 * @param ctx the parse tree
	 */
	void exitBloco(MinhaLinguagemParser.BlocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(MinhaLinguagemParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(MinhaLinguagemParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#variavelDecl}.
	 * @param ctx the parse tree
	 */
	void enterVariavelDecl(MinhaLinguagemParser.VariavelDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#variavelDecl}.
	 * @param ctx the parse tree
	 */
	void exitVariavelDecl(MinhaLinguagemParser.VariavelDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(MinhaLinguagemParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(MinhaLinguagemParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#cmdLeia}.
	 * @param ctx the parse tree
	 */
	void enterCmdLeia(MinhaLinguagemParser.CmdLeiaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#cmdLeia}.
	 * @param ctx the parse tree
	 */
	void exitCmdLeia(MinhaLinguagemParser.CmdLeiaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#cmdEscreva}.
	 * @param ctx the parse tree
	 */
	void enterCmdEscreva(MinhaLinguagemParser.CmdEscrevaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#cmdEscreva}.
	 * @param ctx the parse tree
	 */
	void exitCmdEscreva(MinhaLinguagemParser.CmdEscrevaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#cmdSe}.
	 * @param ctx the parse tree
	 */
	void enterCmdSe(MinhaLinguagemParser.CmdSeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#cmdSe}.
	 * @param ctx the parse tree
	 */
	void exitCmdSe(MinhaLinguagemParser.CmdSeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MinhaLinguagemParser#cmdEnquanto}.
	 * @param ctx the parse tree
	 */
	void enterCmdEnquanto(MinhaLinguagemParser.CmdEnquantoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MinhaLinguagemParser#cmdEnquanto}.
	 * @param ctx the parse tree
	 */
	void exitCmdEnquanto(MinhaLinguagemParser.CmdEnquantoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprNao}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprNao(MinhaLinguagemParser.ExprNaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprNao}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprNao(MinhaLinguagemParser.ExprNaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprString}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprString(MinhaLinguagemParser.ExprStringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprString}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprString(MinhaLinguagemParser.ExprStringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprNumero}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprNumero(MinhaLinguagemParser.ExprNumeroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprNumero}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprNumero(MinhaLinguagemParser.ExprNumeroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprMultDiv}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprMultDiv(MinhaLinguagemParser.ExprMultDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprMultDiv}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprMultDiv(MinhaLinguagemParser.ExprMultDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprIgual}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprIgual(MinhaLinguagemParser.ExprIgualContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprIgual}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprIgual(MinhaLinguagemParser.ExprIgualContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprParenteses}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprParenteses(MinhaLinguagemParser.ExprParentesesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprParenteses}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprParenteses(MinhaLinguagemParser.ExprParentesesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprId}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprId(MinhaLinguagemParser.ExprIdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprId}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprId(MinhaLinguagemParser.ExprIdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprLogica}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprLogica(MinhaLinguagemParser.ExprLogicaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprLogica}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprLogica(MinhaLinguagemParser.ExprLogicaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprSomaSub}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExprSomaSub(MinhaLinguagemParser.ExprSomaSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprSomaSub}
	 * labeled alternative in {@link MinhaLinguagemParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExprSomaSub(MinhaLinguagemParser.ExprSomaSubContext ctx);
}