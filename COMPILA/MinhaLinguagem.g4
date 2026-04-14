grammar MinhaLinguagem;

// --- REGRAS SINTÁTICAS (PARSER) ---
programa: pacote declaracaoFunc+ EOF;

pacote: 'pacote' ID ; // Ex: pacote principal

declaracaoFunc: 'func' ID '(' ')' bloco ; // Ex: func principal() { ... }

bloco: '{' comando* '}' ;

comando
    : variavelDecl
    | atribuicao
    | cmdLeia
    | cmdEscreva
    | cmdSe
    | cmdEnquanto
    ;

// Estilo Go: var <nome> <tipo> = <valor>
variavelDecl: 'var' ID TIPO ('=' expressao)? ;

atribuicao: ID '=' expressao ;

cmdLeia: 'leia' '(' ID ')' ;

cmdEscreva: 'escreva' '(' expressao ')' ;

// "se...então...senão" com blocos de chaves
cmdSe: 'se' expressao 'entao' bloco ('senao' bloco)? ;

// "enquanto...faça"
cmdEnquanto: 'enquanto' expressao 'faca' bloco ;

expressao
    : '(' expressao ')'                                # ExprParenteses
    | NAO expressao                                    # ExprNao
    | expressao (MULT | DIV) expressao                 # ExprMultDiv
    | expressao (SOMA | SUB) expressao                 # ExprSomaSub
    | expressao IGUAL expressao                        # ExprIgual
    | expressao (E_LOGICO | OU_LOGICO) expressao       # ExprLogica
    | ID                                               # ExprId
    | NUMERO                                           # ExprNumero
    | STRING_VAL                                       # ExprString
    ;

// --- REGRAS LÉXICAS (SCANNER) ---
TIPO: 'int' | 'string';
NAO: '!';
MULT: '*';
DIV: '/';
SOMA: '+';
SUB: '-';
IGUAL: '==';
E_LOGICO: '&&';
OU_LOGICO: '||';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;
STRING_VAL: '"' ~["]* '"';

WS: [ \t\r\n]+ -> skip; // Ignora espaços
COMENTARIO: '//' ~[\r\n]* -> skip; // Ignora comentários
 
 