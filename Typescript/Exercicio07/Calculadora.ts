/**2. Crie uma classe Calculadora com:
a. Dois tributos privados chamados representando dois operandos;
b. Crie um construtor que inicializa os atributos;
c. Crie um método que retorna a soma dos dois atributos;
d. Teste a classe.

3. Crie uma classe chamada CalculadoraCientifica que herda da classe Calculadora
do exercício passado e:
a. Implemente um método chamado exponenciar que retorne o primeiro
operando elevado ao segundo;
b. Teste a classe;
c. Foi necessária alguma modificação em Calculadora para o acesso aos
atributos? */

class Calculadora{
    // adicionando atributos protegidos para serem acessados por calculadoraCientifica posteriormente
    protected operando1: number;
    protected operando2: number;

    // inicializando os atributos
    constructor (operando1: number, operando2:number){
        this.operando1 = operando1;
        this.operando2 = operando2;
    }

    // métodos operacionais
    public soma():number{
        return this.operando1 + this.operando2;
    }
    public multiplicacao(): number{
        return this.operando1 * this.operando2
    }
}

// testando calculadora
var calculo = new Calculadora(10, 2);
console.log(`Soma: ${calculo.soma()}`); // 12
console.log(`Multiplicacao: ${calculo.multiplicacao()}`); // 20

class CalculadoraCientifica extends Calculadora{
    exponenciar(): number{
        return this.operando1 ** this.operando2;
    }
}

// testando calculadoraCientifica
var calculoCientifico = new CalculadoraCientifica(10,2);
console.log(`o resultado da exponenciação é: ${calculoCientifico.exponenciar()}`) // 100

/**
 c. Foi necessária alguma modificação em Calculadora para o acesso aosatributos?
 Foi necessário tirar a privacidade dos operandos 1 e 2 e transformá-los em protegidos para realizar o método exponenciar, visto que quando os operandos estão privados eles só podem ser acessados pela classe calculadora, mas quando estão protegidos além de poderem ser acessados pela classe calculadora eles também podem ser acessados por suas subclasses (como no caso de calculadoraCientifica que é uma subclasse de calculadora).*/