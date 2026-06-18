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
    let a = 0;
    let b = 0;
    let c = 0;
    console.log("Digite o lado A:");
    a = parseInt(__leia());
    console.log("Digite o lado B:");
    b = parseInt(__leia());
    console.log("Digite o lado C:");
    c = parseInt(__leia());
    if (a <= 0 || b <= 0 || c <= 0) {
        console.log("Medidas invalidas");
    }
    if (a > 0 && b > 0 && c > 0) {
        if (a === b && b === c) {
            console.log("Triangulo equilatero");
        }
        if (a !== b && b !== c && a !== c) {
            console.log("Triangulo escaleno");
        }
    }
}

principal();
