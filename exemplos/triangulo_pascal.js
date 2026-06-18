// Codigo JavaScript gerado pelo compilador Mini Go (transpilador)
// Execute com: node arquivo.js
'use strict';

let __entrada = null, __pos = 0;
function __leia() {
    if (__entrada === null) {
        __entrada = require('fs').readFileSync(0, 'utf8')
                    .split(/\s+/).filter(s => s.length > 0);
    }
    return __entrada[__pos++];
}

function principal() {
    let n = 0;
    console.log("Digite o numero de linhas do triangulo (n >= 1):");
    n = parseInt(__leia());
    if (n <= 0) {
        console.log("Erro: n deve ser maior ou igual a 1");
    }
    if (n > 0) {
        let i = 0;
        while (i < n) {
            let valor = 1;
            let j = 0;
            while (j <= i) {
                console.log(valor);
                valor = Math.trunc(valor * (i - j) / (j + 1));
                j = j + 1;
            }
            i = i + 1;
        }
    }
}

principal();
