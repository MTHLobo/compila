# ==============================================================
#  gerador.py  —  Gerador de Código Final do Compilador Mini Go
#  Disciplina: Compiladores — IFMT, Engenharia de Computação
#
#  FASE 4 (back-end): traduz a AST validada para JavaScript.
#  Como a linguagem-alvo (JS) também é de alto nível, esta etapa
#  é uma TRANSPILAÇÃO (tradução source-to-source), e não a
#  geração de código de máquina de um compilador tradicional.
#  A linguagem-alvo (JavaScript) é DIFERENTE da inspiração (Go),
#  conforme a exigência da etapa final.
#
#  Como usar (já integrado no main.py):
#
#      from gerador import GeradorCodigo
#      gerador = GeradorCodigo()
#      codigo = gerador.gerar(tree, parser)
#      gerador.exibir_log()
#      # ... grava o .js em disco
#
#  Mapeamento principal:
#      var x int        -> let x = 0
#      var x string     -> let x = ""
#      leia(x)          -> x = parseInt(__leia())   | x = __leia()
#      escreva(e)       -> console.log(e)
#      se/senao         -> if/else
#      enquanto         -> while
#      a / b            -> Math.trunc(a / b)   (mantém divisão inteira)
#      ==  !=           -> ===  !==            (igualdade estrita)
# ==============================================================

from MinhaLinguagemParser import MinhaLinguagemParser


class GeradorCodigo:

    def __init__(self):
        self.linhas  = []      # linhas do programa JS de saída
        self.log     = []      # log de operações de geração
        self.indent  = 1       # nível de indentação dentro de uma função
        self.escopos = [{}]    # pilha de escopos: nome -> "int" | "string"

    # ── escopos (espelham os escopos da análise semântica) ────
    def _entrar(self):
        self.escopos.append({})

    def _sair(self):
        if len(self.escopos) > 1:
            self.escopos.pop()

    def _declarar(self, nome, tipo):
        self.escopos[-1][nome] = tipo

    def _tipo_de(self, nome):
        for escopo in reversed(self.escopos):
            if nome in escopo:
                return escopo[nome]
        return "int"   # fallback (não deveria ocorrer após a semântica)

    # ── emissão ───────────────────────────────────────────────
    def _emitir(self, txt):
        self.linhas.append("    " * self.indent + txt)

    def _log(self, msg):
        self.log.append(f"  [GER] {msg}")

    # ── ponto de entrada ──────────────────────────────────────
    def gerar(self, tree, parser):
        """Recebe a árvore do parser ANTLR4 e devolve o código JS como string."""
        self._log("Início da transpilação (linguagem-alvo: JavaScript).")

        # Cabeçalho: leitor de entrada (stdin) sem dependências externas.
        # A leitura é preguiçosa: só lê o stdin se o programa usar 'leia'.
        self.linhas.append("// Codigo JavaScript gerado pelo compilador Mini Go (transpilador)")
        self.linhas.append("// Execute com: node arquivo.js")
        self.linhas.append("'use strict';")
        self.linhas.append("")
        self.linhas.append("let __entrada = null, __pos = 0;")
        self.linhas.append("function __leia() {")
        self.linhas.append("    if (__entrada === null) {")
        self.linhas.append("        __entrada = require('fs').readFileSync(0, 'utf8')")
        self.linhas.append("                    .split(/\\s+/).filter(s => s.length > 0);")
        self.linhas.append("    }")
        self.linhas.append("    return __entrada[__pos++];")
        self.linhas.append("}")
        self.linhas.append("")
        self._log("Cabeçalho emitido: 'use strict' + leitor de stdin __leia().")

        funcs = tree.declaracaoFunc()
        for func in funcs:
            self._gerar_func(func)

        # Chamada da função de entrada 'principal'
        nomes = [f.ID().getText() for f in funcs]
        entrada = "principal" if "principal" in nomes else nomes[0]
        self.linhas.append(f"{entrada}();")
        self._log(f"Chamada de entrada emitida: '{entrada}()'.")

        self._log("Fim da transpilação.")
        return "\n".join(self.linhas) + "\n"

    def exibir_log(self):
        print("\n" + "=" * 56)
        print("  LOG DO GERADOR DE CÓDIGO (TRANSPILADOR)")
        print("=" * 56)
        for linha in self.log:
            print(linha)
        print("=" * 56)

    # ── função ────────────────────────────────────────────────
    def _gerar_func(self, ctx):
        nome = ctx.ID().getText()
        self._log(f"Gerando função '{nome}' → function {nome}()")
        self.linhas.append(f"function {nome}() {{")
        self._entrar()
        self.indent = 1
        self._gerar_comandos(ctx.bloco())
        self._sair()
        self.linhas.append("}")
        self.linhas.append("")

    # ── bloco (apenas os comandos; as chaves são do chamador) ──
    def _gerar_comandos(self, bloco_ctx):
        for cmd in bloco_ctx.comando():
            self._gerar_no(cmd.getChild(0))

    # ── dispatcher de comandos ────────────────────────────────
    def _gerar_no(self, ctx):
        if isinstance(ctx, MinhaLinguagemParser.VariavelDeclContext):
            return self._g_decl(ctx)
        if isinstance(ctx, MinhaLinguagemParser.AtribuicaoContext):
            return self._g_atrib(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdLeiaContext):
            return self._g_leia(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdEscrevaContext):
            return self._g_escreva(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdSeContext):
            return self._g_se(ctx)
        if isinstance(ctx, MinhaLinguagemParser.CmdEnquantoContext):
            return self._g_enquanto(ctx)

    # ── declaração de variável ────────────────────────────────
    def _g_decl(self, ctx):
        nome = ctx.ID().getText()
        tipo = ctx.TIPO().getText()
        self._declarar(nome, tipo)

        if ctx.expressao():
            self._emitir(f"let {nome} = {self._expr(ctx.expressao())};")
        else:
            padrao = "0" if tipo == "int" else '""'
            self._emitir(f"let {nome} = {padrao};")
        self._log(f"variavelDecl '{nome}':{tipo} → 'let' emitido.")

    # ── atribuição ────────────────────────────────────────────
    def _g_atrib(self, ctx):
        nome = ctx.ID().getText()
        self._emitir(f"{nome} = {self._expr(ctx.expressao())};")
        self._log(f"atribuicao '{nome}' → código JS emitido.")

    # ── leia ──────────────────────────────────────────────────
    def _g_leia(self, ctx):
        nome = ctx.ID().getText()
        tipo = self._tipo_de(nome)
        if tipo == "string":
            self._emitir(f"{nome} = __leia();")
        else:
            self._emitir(f"{nome} = parseInt(__leia());")
        self._log(f"cmdLeia '{nome}' → __leia() emitido ({tipo}).")

    # ── escreva ───────────────────────────────────────────────
    def _g_escreva(self, ctx):
        # console.log já lida com número e string e adiciona quebra de linha.
        self._emitir(f"console.log({self._expr(ctx.expressao())});")
        self._log("cmdEscreva → console.log emitido.")

    # ── se / senao ────────────────────────────────────────────
    def _g_se(self, ctx):
        cond = self._expr(ctx.expressao())
        self._log(f"cmdSe → if ({cond}) emitido.")
        self._emitir(f"if ({cond}) {{")
        self.indent += 1
        self._entrar()
        self._gerar_comandos(ctx.bloco(0))
        self._sair()
        self.indent -= 1

        blocos = ctx.bloco()
        if len(blocos) > 1:           # tem 'senao'
            self._emitir("} else {")
            self.indent += 1
            self._entrar()
            self._gerar_comandos(blocos[1])
            self._sair()
            self.indent -= 1
        self._emitir("}")

    # ── enquanto ──────────────────────────────────────────────
    def _g_enquanto(self, ctx):
        cond = self._expr(ctx.expressao())
        self._log(f"cmdEnquanto → while ({cond}) emitido.")
        self._emitir(f"while ({cond}) {{")
        self.indent += 1
        self._entrar()
        self._gerar_comandos(ctx.bloco())
        self._sair()
        self.indent -= 1
        self._emitir("}")

    # ── expressões → string JS ────────────────────────────────
    def _expr(self, ctx):
        if isinstance(ctx, MinhaLinguagemParser.ExprParentesesContext):
            return f"({self._expr(ctx.expressao())})"

        if isinstance(ctx, MinhaLinguagemParser.ExprNaoContext):
            return f"!({self._expr(ctx.expressao())})"

        if isinstance(ctx, MinhaLinguagemParser.ExprMultDivContext):
            op  = ctx.getChild(1).getText()
            esq = self._expr(ctx.expressao(0))
            dir = self._expr(ctx.expressao(1))
            if op == "/":
                # JS divide em ponto flutuante; Math.trunc preserva o
                # comportamento de divisão inteira da linguagem-fonte.
                return f"Math.trunc({esq} / {dir})"
            return f"{esq} * {dir}"

        if isinstance(ctx, MinhaLinguagemParser.ExprSomaSubContext):
            op = ctx.getChild(1).getText()
            return f"{self._expr(ctx.expressao(0))} {op} {self._expr(ctx.expressao(1))}"

        if isinstance(ctx, MinhaLinguagemParser.ExprRelacionalContext):
            op = ctx.getChild(1).getText()
            # igualdade estrita em JS evita coerções inesperadas
            if op == "==":
                op = "==="
            elif op == "!=":
                op = "!=="
            return f"{self._expr(ctx.expressao(0))} {op} {self._expr(ctx.expressao(1))}"

        if isinstance(ctx, MinhaLinguagemParser.ExprLogicaContext):
            op = ctx.getChild(1).getText()
            return f"{self._expr(ctx.expressao(0))} {op} {self._expr(ctx.expressao(1))}"

        if isinstance(ctx, MinhaLinguagemParser.ExprIdContext):
            return ctx.ID().getText()

        if isinstance(ctx, MinhaLinguagemParser.ExprNumeroContext):
            return ctx.NUMERO().getText()

        if isinstance(ctx, MinhaLinguagemParser.ExprStringContext):
            return ctx.STRING_VAL().getText()

        return "0 /* expr desconhecida */"
