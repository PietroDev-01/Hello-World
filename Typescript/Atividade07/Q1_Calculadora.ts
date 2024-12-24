/**1. Crie uma classe Calculadora que tenha:
a. Dois atributos privados (operando1 e 2) do tipo number;
b. Dois métodos públicos, cada um representando uma operação básica;
c. Um construtor onde são passados os operandos e que esses inicializam os
atributos;
Teste a classe calculadora e seus métodos. Tente acessar os atributos
diretamente e verifique o que acontece. */

class Calculadora{
    private operando1: number;
    private operando2: number;

    constructor (operando1: number, operando2:number){
        this.operando1 = operando1;
        this.operando2 = operando2;
    }
    public soma():number{
        return this.operando1 + this.operando2;
    }

    public multiplicacao(): number{
        return this.operando1 * this.operando2
    }
}

var calculo = new Calculadora(10, 2);

// Chamando métodos
console.log(`Soma: ${calculo.soma()}`); // 12
console.log(`Multiplicacao: ${calculo.multiplicacao()}`); // 20

// Tentandoo acessar os atributos diretamente
console.log(calculo.operando1); // Erro: Property 'operando1' is private and only accessible within class 'Calculadora'.
console.log(calculo.operando2); // Erro: Property 'operando2' is private and only accessible within class 'Calculadora'.