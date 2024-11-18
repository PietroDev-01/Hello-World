/*10. Crie uma classe chamada Jogador e nela:
• Crie 3 atributos inteiros representando força, nível e pontos atuais;
• Crie um construtor no qual os 3 parâmetros são passados e inicialize os
respectivos atributos;
• Crie um método chamado calcularAtaque. Nele, calcule e retorne o valor da
multiplicação de força pelo nível. Esse resultado é o dano de ataque do
jogador;
• Crie um método chamado atacar em que é passado um outro jogador
(atacado) como parâmetro. Nele e é feita a subtração do dano (método
calcularAtaque) dos pontos do atacado;
• Crie um método chamado estaVivo que retorna true caso o atributo pontos
do jogador seja maior que zero e falso caso contrário.
• Altere o método atacar para usar o método está vivo e desconsiderar a
operação, ou seja, não atacar, caso o jogador passado por parâmetro não
esteja vivo.
• Crie um método chamado toString() que retorna a representação textual do
jogador concatenando todos os seus atributos.
• Avalie em com testes dois jogadores instanciados e inicializados através do
construtor. Utilize o método de ataque de cada jogador e ao final, verifique
qual jogador tem mais pontos.
*/

class Jogador {
    forca: number;
    nivel: number;
    pontosAtuais: number;

    constructor(forca: number, nivel: number, pontosAtuais: number) {
        this.forca = forca;
        this.nivel = nivel;
        this.pontosAtuais = pontosAtuais;
    }

    // Calcula o dano de ataque
    calcularAtaque(): number {
        return this.forca * this.nivel;
    }

    // Método para atacar outro jogador
    atacar(atacado: Jogador): void {
        if (atacado.estaVivo()) { // Só ataca se o jogador atacado estiver vivo
            const dano = this.calcularAtaque();
            atacado.pontosAtuais -= dano;
        }
    }

    // Verifica se o jogador está vivo (pontos > 0)
    estaVivo(): boolean {
        return this.pontosAtuais > 0;
    }

    // Representação textual do jogador
    toString(): string {
        return `Jogador - Força: ${this.forca}, Nível: ${this.nivel}, Pontos Atuais: ${this.pontosAtuais}`;
    }
}

// Testando a classe com dois jogadores
let jogador1 = new Jogador(10, 5, 100);
let jogador2 = new Jogador(8, 6, 90);

// Jogador1 ataca jogador2
jogador1.atacar(jogador2);
console.log(jogador1.toString()); // Exibe os atributos de jogador1
console.log(jogador2.toString()); // Exibe os atributos de jogador2 após o ataque

// Jogador2 ataca jogador1
jogador2.atacar(jogador1);
console.log(jogador1.toString()); // Exibe os atributos de jogador1 após ser atacado
console.log(jogador2.toString()); // Exibe os atributos de jogador2

// Verificando qual jogador tem mais pontos
if (jogador1.pontosAtuais > jogador2.pontosAtuais) {
    console.log("Jogador 1 tem mais pontos.");
} else if (jogador2.pontosAtuais > jogador1.pontosAtuais) {
    console.log("Jogador 2 tem mais pontos.");
} else {
    console.log("Ambos os jogadores têm a mesma quantidade de pontos.");
}
