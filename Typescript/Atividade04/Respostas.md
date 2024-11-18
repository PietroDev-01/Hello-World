# Questões sobre Tipagem e Inicialização em Programação

## 1. Assinale verdadeiro ou falso:
- ( ) Objetos são modelos para classes;
- ( ) Atributos de uma classe devem ser obrigatoriamente inicializados para que as classes compilem;
- ( ) Uma variável declarada dentro de um método deve ser inicializada para que a classe seja compilável;
- ( ) Uma variável que seja uma classe declarada em um método é automaticamente inicializada com undefined;
- ( ) Construtores são rotinas especiais que servem para inicializar e configurar os objetos no momento da instanciação;
- ( ) Construtores não possuem tipo de retorno e podem ou não ter parâmetros;
- ( ) Uma classe pode ter várias instâncias.

**Respostas:** F, F, F, V, V, V, V

## 2. Problema de compilação na classe `Hotel`

```typescript
class Hotel {
    quantReservas: number;
    
    adicionarReserva(): void {
        this.quantReservas++;
    }
}
```

Justificativa: Sim, a variável será considerada indefinida ("undefined"). A variável quantReservas não inicia sendo igual a 0, o que causará um erro de compilação na execução do método adicionarReserva(), pois ele tenta incrementar em 1 uma variável indefinida.
















## 3. Ainda sobre a classe do exemplo anterior, considere o código abaixo: 
let hotel : Hotel = new Hotel(2);
console.log(hotel.quantReservas);
Adicione o construtor que aceite um parâmetro inteiro e faça a inicialização do atributo quantReservas.

**Respostas:**
```Typescript
class Hotel {
    quantReservas: number;

    constructor(quantReservas: number) {
        this.quantReservas = quantReservas;
    }

    adicionarReserva(): void {
        this.quantReservas++;
    }
}

let hotel: Hotel = new Hotel(2);
console.log(hotel.quantReservas); // Saída: 2

```

## 4. Considere a classe Radio e as instruções que fazem seu uso abaixo:
class Radio {
    volume : number;

    constructor(volume : number) {
        this.volume = volume;
    }
}
let r : Radio = new Radio();
r.volume = 10;
Justifique o erro de compilação e proponha uma solução.

**Respostas:** O erro de compilação ocorre porque a classe Radio define um construtor que exige um parâmetro volume, mas, ao criar uma instância da classe com new Radio(), nenhum argumento foi passado para o construtor.
Para resolver o problema basta atribuir um valor padrão a variável volume

```Typescript
class Radio {
    volume: number;
    
    constructor(volume: number = 0) { // Valor padrão de 0
        this.volume = volume;
    }
}

let r: Radio = new Radio(); // Agora o construtor pode ser chamado sem argumentos
r.volume = 10;

```

## 5. Considerando o uso da classe Conta apresentada em aula e seu uso abaixo:
let c1: Conta = new Conta("1",100);
let c2: Conta = new Conta("2",100);
let c3: Conta;
c1 = c2;
c3 = c1;
c1.sacar(10);
c1.transferir(c2,50);
console.log(c1.consultarSaldo());
console.log(c2.consultarSaldo());
console.log(c3.consultarSaldo());
a. Qual o resultado dos dois "prints"? Justifique sua resposta.
b. O que acontece com o objeto para o qual a referência c1 apontava?

**Respostas:**
a. c1 = 90 c2 = 90 c3 = 90 
Já que c1, c2 e c3 agora apontam para essa mesma conta.

c1.sacar(10); – Reduz o saldo da conta "2" de 100 para 90.
c1.transferir(c2, 50); – Transfere 50 da conta "2" para ela mesma (já que c1 e c2 apontam para o mesmo objeto). Esse saque e depósito não alteram o saldo, pois é uma transferência para a mesma conta.
Após essas operações, o saldo da conta "2" permanece em 90.

b. Foi destruido

## 11. A abordagem da questão 9 é retornar códigos de erro ou acerto. Já a da questão 10 é desconsiderar a alteração. Quais das duas você acha mais correta? Compare com seus códigos escritos em outras disciplinas. 

**Respostas:**
Ambas as abordagens são adequadas para diferentes contextos:

Questão 9 (retornar código de sucesso/falha) é mais apropriada quando o controle preciso é fundamental, como em sistemas críticos ou operações onde é essencial confirmar o resultado (finanças, transações, banco de dados).
Questão 10 (ignorar a operação se não for válida) é ideal para cenários onde a interação entre objetos é baseada em estados dinâmicos e onde o resultado da operação é menos crítico — a fluidez é mais importante que o controle preciso, típico em aplicações de simulação ou jogo.
A escolha depende de fatores como o nível de controle e a complexidade desejada no programa, embora eu ache mais divertida a abordagem da questão 10.