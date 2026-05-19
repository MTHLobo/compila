# ==============================================================
#  semantico.py  —  Analisador Semântico do Compilador Mini Go
#  Disciplina: Compiladores — IFMT, Engenharia de Computação
#
#  Como usar: adicione ao final do main.py existente:
#
#      from semantico import AnalisadorSemantico
#      semantico = AnalisadorSemantico()
#      semantico.analisar(tree, parser)
#      semantico.exibir_resultado()
#
#  O resto do main.py permanece IGUAL.
# ==============================================================

from MinhaLinguagemParser import MinhaLinguagemParser


# ──────────────────────────────────────────────────────────────
#  Tabela de Símbolos com escopos aninhados
# ──────────────────────────────────────────────────────────────
class TabelaSimbolos:
    def __init__(self):
        self._pilha = [{}]   # escopo global

    def entrar(self):
        self._pilha.append({})

    def sair(self):
        if len(self._pilha) > 1:
            self._pilha.pop()

    def declarar(self, nome, tipo, linha):
        """Retorna False se já existir no escopo atual."""
        escopo = self._pilha[-1]
        if nome in escopo:
            return False, escopo[nome]["linha"]
        escopo[nome] = {"tipo": tipo, "linha": linha}
        return True, None

    def buscar(self, nome):
        """Busca do escopo mais interno para o mais externo."""
        for escopo in reversed(self._pilha):
            if nome in escopo:
                return escopo[nome]
        return None


# ──────────────────────────────────────────────────────────────
#  Analisador Semântico
# ──────────────────────────────────────────────────────────────
class AnalisadorSemantico:

    def __init__(self):
        self.tabela  = TabelaSimbolos()
        self.erros   = []
        self.log     = []

    # ── helpers ───────────────────────────────────────────────
    def _erro(self, codigo, msg, ctx):
        linha  = ctx.start.line   if ctx.start  else "?"
        coluna = ctx.start.column if ctx.start  else "?"
        texto  = f"[ERRO SEMÂNTICO - {codigo}] Linha {linha}, Coluna {coluna}: {msg}"
        self.erros.append(texto)
        print(texto)

    def _log(self, msg):
        self.log.append(f"  [SEM] {msg}")

    # ── ponto de entrada ─────────────────────────────────────
    def analisar(self, tree, parser):
        """Recebe a árvore gerada pelo parser ANTLR4 e executa a análise."""
        self._log("Início da análise semântica.")
        self._visitar(tree)
        self._log("Fim da análise semântica.")

    def exibir_resultado(self):
        print("\n" + "=" * 56)
        print("  LOG DO ANALISADOR SEMÂNTICO")
        print("=" * 56)
        for linha in self.log:
            print(linha)
        print("=" * 56)
        if self.erros:
            print(f"\n  {len(self.erros)} ERRO(S) SEMÂNTICO(S) ENCONTRADO(S).")
        else:
            print("\n  SUCESSO: Análise Semântica concluída sem erros!")
        print()

    # ── dispatcher ───────────────────────────────────────────
    def _visitar(self, ctx):
        if ctx is None:
            return None

        nome_classe = type(ctx).__name__

        if isinstance(ctx, MinhaLinguagemParser.ProgramaContext):
            return self._visitar_programa(ctx)
        if isinstance(ctx, MinhaLinguagemParser.DeclaracaoFuncContext):
            return self._visitar_func(ctx)
        if isinstance(ctx, MinhaLinguagemParser.BlocoContext):
            return self._visitar_bloco(ctx)
        if isinstance(ctx, MinhaLinguagemParser.VariavelDeclContext):
            return self._visitar_decl_var(ctx)
        if isinstance(ctx, MinhaLinguagemParser.AtribuicaoContext):
            return self._visitar_atribuicao(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdLeiaContext):
            return self._visitar_leia(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdEscrevaContext):
            return self._visitar_escreva(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdSeContext):
            return self._visitar_se(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdEnquantoContext):
            return self._visitar_enquanto(ctx)

        # Expressões
        if isinstance(ctx, MinhaLinguagemParser.ExprIdContext):
            return self._visitar_expr_id(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprNumeroContext):
            return self._visitar_expr_numero(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprStringContext):
            return self._visitar_expr_string(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprParentesesContext):
            return self._visitar(ctx.expressao())
        if isinstance(ctx, MinhaLinguagemParser.ExprNaoContext):
            return self._visitar_expr_nao(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprMultDivContext):
            return self._visitar_expr_multdiv(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprSomaSubContext):
            return self._visitar_expr_somasub(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprRelacionalContext):
            return self._visitar_expr_relacional(ctx)
        if isinstance(ctx, MinhaLinguagemParser.ExprLogicaContext):
            return self._visitar_expr_logica(ctx)

        # Nó genérico: visita filhos
        for i in range(ctx.getChildCount()):
            self._visitar(ctx.getChild(i))
        return None

    # ── programa ─────────────────────────────────────────────
    def _visitar_programa(self, ctx):
        self._log(f"Visitando: programa (pacote '{ctx.pacote().ID().getText()}')")
        for func in ctx.declaracaoFunc():
            self._visitar_func(func)

    # ── função ───────────────────────────────────────────────
    def _visitar_func(self, ctx):
        nome = ctx.ID().getText()
        self._log(f"Visitando: declaracaoFunc → '{nome}'")
        self.tabela.entrar()
        self._log(f"Ação semântica: novo escopo para função '{nome}'")
        self._visitar_bloco(ctx.bloco())
        self.tabela.sair()
        self._log(f"Ação semântica: escopo da função '{nome}' encerrado")

    # ── bloco ─────────────────────────────────────────────────
    def _visitar_bloco(self, ctx):
        self._log("Visitando: bloco { }")
        for cmd in ctx.comando():
            self._visitar(cmd.getChild(0))  # desce para a regra concreta

    # ── declaração de variável ────────────────────────────────
    def _visitar_decl_var(self, ctx):
        nome = ctx.ID().getText()
        tipo = ctx.TIPO().getText()   # 'int' ou 'string'
        linha = ctx.start.line

        self._log(f"Visitando: variavelDecl → '{nome}' : {tipo} (linha {linha})")

        # Verifica inicializador (tipo compatível)
        tipo_inic = None
        if ctx.expressao():
            tipo_inic = self._visitar(ctx.expressao())

        if tipo_inic is not None and tipo_inic != tipo:
            # Permite inteiro literal em variável string? Não — reporta erro.
            self._erro("SEM-04",
                f"Tipo incompatível: variável '{nome}' é '{tipo}', "
                f"mas recebe valor do tipo '{tipo_inic}'.", ctx)

        # [SEM-02] Declaração duplicada
        ok, linha_orig = self.tabela.declarar(nome, tipo, linha)
        if not ok:
            self._erro("SEM-02",
                f"Variável '{nome}' já declarada (primeira vez na linha {linha_orig}).", ctx)
        else:
            self._log(f"Ação semântica [SEM-02]: '{nome}' declarada. Não é duplicata. OK.")

    # ── atribuição ────────────────────────────────────────────
    def _visitar_atribuicao(self, ctx):
        nome = ctx.ID().getText()
        linha = ctx.start.line
        self._log(f"Visitando: atribuicao → '{nome}' = ... (linha {linha})")

        # [SEM-01] Declaração prévia
        simbolo = self.tabela.buscar(nome)
        if simbolo is None:
            self._erro("SEM-01",
                f"Variável '{nome}' usada sem ter sido declarada.", ctx)
            return

        tipo_expr = self._visitar(ctx.expressao())
        if tipo_expr and simbolo["tipo"] != tipo_expr:
            self._erro("SEM-04",
                f"Atribuição inválida: '{nome}' é '{simbolo['tipo']}', "
                f"mas recebe '{tipo_expr}'.", ctx)
        else:
            self._log(f"Ação semântica [SEM-04]: Atribuição de '{nome}' verificada. OK.")

    # ── leia ─────────────────────────────────────────────────
    def _visitar_leia(self, ctx):
        nome = ctx.ID().getText()
        self._log(f"Visitando: cmdLeia → leia({nome})")

        # [SEM-01]
        if self.tabela.buscar(nome) is None:
            self._erro("SEM-01",
                f"Variável '{nome}' usada em 'leia' sem ter sido declarada.", ctx)
        else:
            self._log(f"Ação semântica [SEM-01]: '{nome}' está declarada. OK.")

    # ── escreva ───────────────────────────────────────────────
    def _visitar_escreva(self, ctx):
        self._log("Visitando: cmdEscreva → escreva(...)")
        self._visitar(ctx.expressao())

    # ── se ────────────────────────────────────────────────────
    def _visitar_se(self, ctx):
        self._log("Visitando: cmdSe → se ... entao ...")

        tipo_cond = self._visitar(ctx.expressao())
        # A linguagem usa int como booleano (0/1); string em condição é erro
        if tipo_cond == "string":
            self._erro("SEM-04",
                "Condição do 'se' não pode ser do tipo 'string'.", ctx)
        else:
            self._log("Ação semântica [SEM-04]: Condição do 'se' é numérica. OK.")

        for bloco in ctx.bloco():
            self.tabela.entrar()
            self._visitar_bloco(bloco)
            self.tabela.sair()

    # ── enquanto ─────────────────────────────────────────────
    def _visitar_enquanto(self, ctx):
        self._log("Visitando: cmdEnquanto → enquanto ... faca ...")

        tipo_cond = self._visitar(ctx.expressao())
        if tipo_cond == "string":
            self._erro("SEM-04",
                "Condição do 'enquanto' não pode ser do tipo 'string'.", ctx)
        else:
            self._log("Ação semântica [SEM-04]: Condição do 'enquanto' é numérica. OK.")

        self.tabela.entrar()
        self._visitar_bloco(ctx.bloco())
        self.tabela.sair()

    # ── expressões ────────────────────────────────────────────
    def _visitar_expr_id(self, ctx):
        nome = ctx.ID().getText()
        self._log(f"Visitando: ExprId → '{nome}'")

        # [SEM-01]
        simbolo = self.tabela.buscar(nome)
        if simbolo is None:
            self._erro("SEM-01",
                f"Variável '{nome}' usada sem ter sido declarada.", ctx)
            return None

        self._log(f"Ação semântica [SEM-01]: '{nome}' encontrada. Tipo: '{simbolo['tipo']}'. OK.")
        return simbolo["tipo"]

    def _visitar_expr_numero(self, ctx):
        self._log(f"Visitando: ExprNumero → {ctx.NUMERO().getText()}")
        return "int"

    def _visitar_expr_string(self, ctx):
        self._log(f"Visitando: ExprString → {ctx.STRING_VAL().getText()}")
        return "string"

    def _visitar_expr_nao(self, ctx):
        self._log("Visitando: ExprNao → ! expressao")
        tipo = self._visitar(ctx.expressao())
        if tipo == "string":
            self._erro("SEM-04",
                "Operador '!' não pode ser aplicado a 'string'.", ctx)
        return "int"

    def _visitar_expr_multdiv(self, ctx):
        op = ctx.getChild(1).getText()
        self._log(f"Visitando: ExprMultDiv → expressao '{op}' expressao")

        t_esq = self._visitar(ctx.expressao(0))
        t_dir = self._visitar(ctx.expressao(1))

        # [SEM-03] Divisão por zero (literal)
        if op == "/":
            texto_dir = ctx.expressao(1).getText()
            if texto_dir == "0":
                self._erro("SEM-03",
                    "Divisão por zero detectada (divisor é literal 0).", ctx)
            else:
                self._log("Ação semântica [SEM-03]: Divisor verificado — não é zero literal. OK.")

        # [SEM-04] Tipos
        if t_esq == "string" or t_dir == "string":
            self._erro("SEM-04",
                f"Operação '{op}' requer operandos numéricos, "
                f"mas encontrou '{t_esq}' e '{t_dir}'.", ctx)
        else:
            self._log(f"Ação semântica [SEM-04]: Operação '{op}' com tipos numéricos. OK.")

        return "int"

    def _visitar_expr_somasub(self, ctx):
        op = ctx.getChild(1).getText()
        self._log(f"Visitando: ExprSomaSub → expressao '{op}' expressao")

        t_esq = self._visitar(ctx.expressao(0))
        t_dir = self._visitar(ctx.expressao(1))

        if t_esq == "string" or t_dir == "string":
            self._erro("SEM-04",
                f"Operação '{op}' requer operandos numéricos, "
                f"mas encontrou '{t_esq}' e '{t_dir}'.", ctx)
        else:
            self._log(f"Ação semântica [SEM-04]: Operação '{op}' com tipos numéricos. OK.")

        return "int"

    def _visitar_expr_relacional(self, ctx):
        op = ctx.getChild(1).getText()
        self._log(f"Visitando: ExprRelacional → expressao '{op}' expressao")

        t_esq = self._visitar(ctx.expressao(0))
        t_dir = self._visitar(ctx.expressao(1))

        if t_esq != t_dir:
            self._erro("SEM-04",
                f"Comparação '{op}' entre tipos diferentes: "
                f"'{t_esq}' e '{t_dir}'.", ctx)
        else:
            self._log(f"Ação semântica [SEM-04]: Relacional '{op}' com tipos iguais. OK.")

        return "int"   # resultado booleano representado como int

    def _visitar_expr_logica(self, ctx):
        op = ctx.getChild(1).getText()
        self._log(f"Visitando: ExprLogica → expressao '{op}' expressao")

        t_esq = self._visitar(ctx.expressao(0))
        t_dir = self._visitar(ctx.expressao(1))

        if t_esq == "string" or t_dir == "string":
            self._erro("SEM-04",
                f"Operador lógico '{op}' requer operandos numéricos, "
                f"mas encontrou '{t_esq}' e '{t_dir}'.", ctx)
        else:
            self._log(f"Ação semântica [SEM-04]: Operação lógica '{op}' verificada. OK.")

        return "int"
