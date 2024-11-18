/* 9. Altere a classe conta dos slides conforme as instruções abaixo:
• Altere o método sacar de forma que ele retorne verdadeiro ou falso. Caso o
saque deixe saldo negativo, o mesmo não será realizado, retornando falso;
• Altere o método transferir() para que retorne também um valor lógico e que
não seja feita a transferência caso o sacar() na conta origem não seja
satisfeito;
• Verifique as diferentes operações implementadas.
*/

class Conta {
    numero: string;
    saldo: number;

    constructor(numero: string, saldoInicial: number) {
        this.numero = numero;
        this.saldo = saldoInicial;
    }

    sacar(valor: number): boolean {
        if (this.saldo >= valor) {
            this.saldo -= valor;
            return true; // Saque bem-sucedido
        }
        return false; // Saldo insuficiente, saque não realizado
    }

    depositar(valor: number): void {
        this.saldo += valor;
    }

    consultarSaldo(): number {
        return this.saldo;
    }

    transferir(contaDestino: Conta, valor: number): boolean {
        if (this.sacar(valor)) { // Verifica se o saque foi bem-sucedido
            contaDestino.depositar(valor);
            return true; // Transferência bem-sucedida
        }
        return false; // Saldo insuficiente, transferência não realizada
    }
}

let conta1 = new Conta("1", 100);
let conta2 = new Conta("2", 50);

console.log(conta1.sacar(30));  // true - saque realizado, saldo conta1: 70
console.log(conta1.sacar(80));  // false - saldo insuficiente, saldo conta1: 70
console.log(conta1.consultarSaldo()); // 70

console.log(conta1.transferir(conta2, 50)); // true - transferência realizada
console.log(conta1.consultarSaldo()); // 20
console.log(conta2.consultarSaldo()); // 100

console.log(conta1.transferir(conta2, 25)); // false - saldo insuficiente, transferência não realizada
console.log(conta1.consultarSaldo()); // 20
console.log(conta2.consultarSaldo()); // 100
