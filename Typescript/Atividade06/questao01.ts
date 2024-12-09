/**1. Atualize a implementação da classe Banco com os métodos apresentados em sala
de aula:
a. Consultar por índice, excluir, atualizar, sacar, depositar e transferir
apresentadas em sala. Nota: o transferir deve ter como parâmetros os dois
números de conta, não os objetos e um valor a ser transferido conforme
slide "Esqueleto" de um cadastro.
b. Crie um método transferir que recebe um array de contas destino e realiza
transferências para cada uma delas;
c. Crie 3 métodos: um que retorne a quantidade de contas, outro que retorne
o total de dinheiro depositado em todas as contas. Por fim, crie um método
que retorne a média do saldo das contas chamando os dois métodos
anteriores. */

class Conta {
    id_conta: number;
    numero: string;
    saldo: number;

    constructor(id_conta: number, numero: string, saldo: number = 0) {
        this.id_conta = id_conta;
        this.numero = numero;
        this.saldo = saldo;
    }

    sacar(valor: number): void {
        if (valor > this.saldo) {
            throw new Error("Saldo insuficiente.");
        }
        this.saldo -= valor;
    }

    depositar(valor: number): void {
        if (valor <= 0) {
            throw new Error("Valor de depósito inválido.");
        }
        this.saldo += valor;
    }

    consultarSaldo(): number {
        return this.saldo;
    }

    transferir(contaDestino: Conta, valor: number): void {
        this.sacar(valor);
        contaDestino.depositar(valor);
    }
}

class Banco {
    private contas: Conta[];

    constructor() {
        this.contas = [];
    }

    inserirConta(conta: Conta): void {
        const contaExistente = this.contas.find(c => c.id_conta === conta.id_conta || c.numero === conta.numero);
        if (contaExistente) {
            throw new Error("Conta com o mesmo ID ou número já cadastrada.");
        }
        this.contas.push(conta);
    }

    consultarConta(numero: string): Conta {
        const conta = this.contas.find(c => c.numero === numero);
        if (!conta) {
            throw new Error("Conta não encontrada.");
        }
        return conta;
    }

    consultarContaPorIndice(indice: number): Conta {
        if (indice < 0 || indice >= this.contas.length) {
            throw new Error("Índice fora do intervalo.");
        }
        return this.contas[indice];
    }

    excluirConta(numero: string): void {
        const index = this.contas.findIndex(c => c.numero === numero);
        if (index === -1) {
            throw new Error("Conta não encontrada.");
        }
        this.contas.splice(index, 1);
    }

    atualizarConta(numero: string, novaConta: Conta): void {
        const index = this.contas.findIndex(c => c.numero === numero);
        if (index === -1) {
            throw new Error("Conta não encontrada.");
        }
        this.contas[index] = novaConta;
    }

    sacar(numero: string, valor: number): void {
        const conta = this.consultarConta(numero);
        conta.sacar(valor);
    }

    depositar(numero: string, valor: number): void {
        const conta = this.consultarConta(numero);
        conta.depositar(valor);
    }

    transferir(numeroOrigem: string, numeroDestino: string, valor: number): void {
        const contaOrigem = this.consultarConta(numeroOrigem);
        const contaDestino = this.consultarConta(numeroDestino);
        contaOrigem.transferir(contaDestino, valor);
    }

    transferirParaMultiplasContas(numeroOrigem: string, contasDestino: { numero: string; valor: number }[]): void {
        const contaOrigem = this.consultarConta(numeroOrigem);
        for (const { numero, valor } of contasDestino) {
            const contaDestino = this.consultarConta(numero);
            contaOrigem.transferir(contaDestino, valor);
        }
    }

    quantidadeDeContas(): number {
        return this.contas.length;
    }

    totalDinheiroDepositado(): number {
        return this.contas.reduce((total, conta) => total + conta.consultarSaldo(), 0);
    }

    mediaSaldos(): number {
        const total = this.totalDinheiroDepositado();
        const quantidade = this.quantidadeDeContas();
        return quantidade === 0 ? 0 : total / quantidade;
    }
}

// Testando as classes
const banco = new Banco();

const conta1 = new Conta(1, "111-1", 1000);
const conta2 = new Conta(2, "222-2", 2000);
const conta3 = new Conta(3, "333-3", 3000);

banco.inserirConta(conta1);
banco.inserirConta(conta2);
banco.inserirConta(conta3);

console.log("Total de contas:", banco.quantidadeDeContas()); // 3
console.log("Total depositado:", banco.totalDinheiroDepositado()); // 6000
console.log("Média dos saldos:", banco.mediaSaldos()); // 2000

banco.sacar("111-1", 500);
banco.depositar("222-2", 300);
banco.transferir("333-3", "111-1", 1000);

console.log("Saldo após transferências:");
console.log(banco.consultarConta("111-1").consultarSaldo()); // 1500
console.log(banco.consultarConta("333-3").consultarSaldo()); // 2000

banco.transferirParaMultiplasContas("222-2", [
    { numero: "111-1", valor: 100 },
    { numero: "333-3", valor: 200 },
]);

console.log("Saldos após múltiplas transferências:");
console.log(banco.consultarConta("111-1").consultarSaldo()); // 1600
console.log(banco.consultarConta("333-3").consultarSaldo()); // 2200
console.log(banco.consultarConta("222-2").consultarSaldo()); // 2000
