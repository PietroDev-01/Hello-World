# Tipagem Dinâmica vs. Tipagem Estática

## 1. Qual a diferença entre tipagem dinâmica e tipagem estática?

**Tipagem Dinâmica:**  
A linguagem de programação permite que o tipo da variável seja definido e alterado em tempo de execução. Em outras palavras, o tipo de uma variável é determinado quando o programa é executado, e o mesmo valor pode ser redefinido como outro tipo ao longo do código. Exemplos de linguagens com tipagem dinâmica incluem Python, JavaScript e Ruby.

**Tipagem Estática:**  
O tipo de uma variável é definido em tempo de compilação, antes do programa ser executado. Isso significa que, uma vez declarado o tipo, ele não pode ser alterado. Linguagens com tipagem estática, como Java, C e C++, verificam os tipos durante a compilação, o que evita erros de tipos em tempo de execução.

## 2. Qual o principal problema do uso de tipagem dinâmica?

O principal problema do uso de tipagem dinâmica é a possibilidade de erros em tempo de execução, pois variáveis podem ter seus tipos alterados de maneira inesperada. Isso pode resultar em erros que só são detectados quando o código já está sendo executado, dificultando a depuração e aumentando o risco de comportamentos inesperados.

## 3. Exemplo em que a tipagem dinâmica pode ser problemática

```javascript
let valor = "5";
let resultado = valor + 5;
console.log(resultado); // Resultado é "55" (concatenação, não soma)
```

## 4. Por que dizemos que a linguagem C, mesmo tendo tipagem estática, possui tipagem fraca?

Embora o C seja uma linguagem de tipagem estática, ele possui tipagem fraca porque permite conversões implícitas entre tipos (chamadas de "coerções"). Por exemplo:
```c
#include <stdio.h>

int main() {
    int numero_inteiro = 5;
    double resultado = numero_inteiro / 2; // Divisão inteira atribuída a um double
    printf("%f\n", resultado); // Saída: 2.000000
    return 0;
}
```

Nesse caso, numero_inteiro é um int, mas está sendo dividido por outro int e atribuído a uma variável double. Em C, o compilador não gera erro, mas o resultado da divisão será 2.0, em vez de 2.5, pois o cálculo é feito com inteiros antes da conversão. Esse comportamento é comum em linguagens de tipagem fraca.

## 5. Tipagem do TypeScript é fraca por uma variável do tipo number aceitar tanto inteiros como ponto flutuante?

No TypeScript, não consideramos a tipagem como fraca pelo fato de uma variável number aceitar tanto valores inteiros quanto ponto flutuante. Isso ocorre porque inteiros e floats são subconjuntos do tipo number, representando números de diferentes precisões. Em tipagem fraca, a variável poderia, por exemplo, ser automaticamente convertida para uma string ou outro tipo sem coerções explícitas, o que não ocorre no TypeScript.