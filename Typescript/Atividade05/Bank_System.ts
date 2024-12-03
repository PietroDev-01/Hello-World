class Conta {
    id_conta: number;
    cliente: Cliente;
    numero: string;
    saldo: number;

    constructor(id_conta: number, cliente: Cliente, numero: string, saldo: number = 0) {
        this.id_conta = id_conta;
        this.cliente = cliente;
        this.numero = numero;
        this.saldo = saldo;
    }

    sacar(valor: number): void {
        this.saldo = this.saldo - valor;
    }

    depositar(valor: number): void {
        this.saldo = this.saldo + valor;
    }

    consultarSaldo(): number {
        return this.saldo
    }

    transferir(contaDestino: Conta, valor: number): void {

        this.sacar(valor);
        contaDestino.depositar(valor);
    }
}

class Banco {
    contas: Conta[];
    clientes: Cliente[];

    constructor() {
        this.contas = [];
        this.clientes = [];
    }

    inserir(conta: Conta) {
        this.contas.push(conta);
    }

    consultar(numero: string): Conta {
        let contaProcurada!: Conta;

        for (let conta of this.contas) {
            if (conta.numero == numero) {
                contaProcurada = conta;
                break;
            }
        }

        
        return contaProcurada;
    }

    inserirCliente(cliente: Cliente): void { // Adicionar Clientes - a)
        const clienteExistente = this.clientes.find(c => c.cpf === cliente.cpf);
        if (clienteExistente) {
            throw new Error("Cliente com este CPF já cadastrado.");
        }
        this.clientes.push(cliente);
    }   

    consultarCliente(cpf: string): Cliente { // Consultar cliente pelo cpf - b)
        const cliente = this.clientes.find(c => c.cpf === cpf);
        if (!cliente) {
            throw new Error("Cliente não encontrado.");
        }
        return cliente;
    }

}

class Cliente {
    id: number;
    nome: string;
    cpf: string;
    dataNascimento: Date;
    contas: Conta[];

    constructor(id: number, nome: string, cpf: string, dataNascimento: Date) {
        this.id = id;
        this.nome = nome;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
        this.contas = [];
    }
}



let banco: Banco = new Banco();

banco.inserir(new Conta('111-1', 100));
banco.inserir(new Conta('222-2', 200));

console.log(banco.consultar('111-1'));