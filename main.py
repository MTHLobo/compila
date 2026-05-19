import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener
from MinhaLinguagemLexer import MinhaLinguagemLexer
from MinhaLinguagemParser import MinhaLinguagemParser

# 1. Classe para formatar os erros igual o professor pediu no PDF
class MeuErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(recognizer, Lexer):
            print(f"ERRO LÉXICO [Linha {line}, Coluna {column}]: Símbolo inválido -> {msg}")
        else:
            print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg}")
        sys.exit(1) # Para a execução se achar erro

def main():
   # Verifica se o usuário passou o nome do arquivo no terminal
    if len(sys.argv) > 1:
        arquivo_fonte = sys.argv[1]
    else:
        print("ERRO: Você esqueceu de informar o arquivo!")
        print("Uso correto: python main.py <caminho_do_arquivo>")
        sys.exit(1)
        
    print(f"--- Compilando: {arquivo_fonte} ---\n")

    input_stream = FileStream(arquivo_fonte, encoding='utf-8')
    
    # 2. Analisador Léxico (Scanner)
    lexer = MinhaLinguagemLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MeuErrorListener())
    
    stream = CommonTokenStream(lexer)
    
    # 3. Exigência do PDF: Registre logs detalhados dos Tokens
    stream.fill()
    print("--- LOG DO ANALISADOR LÉXICO ---")
    for token in stream.tokens:
        if token.type != Token.EOF:
            nome_token = f"TOKEN_{token.type}" # Nome de segurança anti-crash
            
            # Bloco blindado: Tenta pegar o nome sem deixar o Python travar
            try:
                if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>":
                    nome_token = lexer.symbolicNames[token.type]
                elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] != "<INVALID>":
                    nome_token = lexer.literalNames[token.type]
            except Exception:
                pass # Se der erro de Index, ele ignora e mantém o nome de segurança
                
            print(f"<Tipo: {nome_token}, Lexema: '{token.text}', Linha: {token.line}, Coluna: {token.column}>")
    print("--------------------------------\n")

    # 4. Analisador Sintático (Parser)
    parser = MinhaLinguagemParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MeuErrorListener())
    
    # Roda a análise a partir da regra raiz 'programa'
    tree = parser.programa()
    
    # Gera a árvore e imprime no terminal
    print("\n--- ÁRVORE SINTÁTICA (Formato LISP) ---")
    print(Trees.toStringTree(tree, None, parser))
    print("\nSUCESSO: Análise Léxica e Sintática concluída sem erros estruturais!")

    # FASE 3: ANÁLISE SEMÂNTICA
    print("\n--- ANÁLISE SEMÂNTICA ---")
    from semantico import AnalisadorSemantico
    semantico = AnalisadorSemantico()
    semantico.analisar(tree, parser)
    semantico.exibir_resultado()

if __name__ == '__main__':
    main()