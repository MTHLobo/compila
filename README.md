# ⚙️ Front-end de Compilador (Léxico e Sintático)

Este projeto consiste no desenvolvimento do *Front-end* de um compilador, implementando as fases de **Análise Léxica** e **Análise Sintática**. O projeto foi construído utilizando a ferramenta **ANTLR4** e o motor de execução em **Python**.

## 📌 Sobre a Linguagem ("Mini Go")
Para este projeto, foi criada uma linguagem didática com tipagem estática e estruturas de controle. A gramática foi fortemente inspirada na sintaxe da linguagem **Go**, porém adaptada e traduzida para o português para fins acadêmicos.

**Características da Gramática:**
- Declaração de funções (`func`) e variáveis (`var`).
- Estruturas de decisão (`se ... entao`).
- Estruturas de repetição (`enquanto ... faca`).
- Funções de entrada e saída (`leia` e `escreva`).
- Blocos delimitados por chaves `{ }` e ausência de ponto e vírgula obrigatório.

## 🚀 Como Funciona

1. **Analisador Léxico (Scanner):** Lê o arquivo fonte (`teste.txt`), ignora espaços e comentários, e gera uma fita de Tokens. O sistema emite logs detalhados de cada token reconhecido (Tipo, Lexema, Linha e Coluna).
2. **Analisador Sintático (Parser):** Consome os tokens gerados e valida a estrutura gramatical. Em caso de sucesso, gera a Árvore de Sintaxe Abstrata (AST).
3. **Tratamento de Erros:** Classes customizadas interceptam falhas. Códigos mal formados interrompem a compilação indicando o local exato da falha (ex: `ERRO SINTÁTICO [Linha X, Coluna Y]`).

## 💻 Como Executar

Certifique-se de ter o Python 3 e o runtime do ANTLR4 instalados:
```bash
pip install antlr4-python3-runtime==4.13.2
