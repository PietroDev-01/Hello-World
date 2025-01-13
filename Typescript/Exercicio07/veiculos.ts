/**1. As classes Carro, Veiculo e CarroEletrico são bem semelhantes. Reescreva as
classes usando herança para que os atributos duplicados não sejam mais
necessários.*/
class Veiculo {
    // adicionando atributos protegidos para serem acessados pelas subclasses de veiculo
    protected placa: string;
    protected ano: number;
    protected modelo: string;

    // inicializando atributos
    constructor(placa: string, ano: number, modelo: string){
        this.placa = placa;
        this.modelo = modelo;
        this.ano = ano;
    }
}

class Carro extends Veiculo{
    ligar(): string{
        return "BROOOOOOOMMMMMMMMM"; // tá potente <*-*>
    }
}

class CarroEletrico extends Veiculo{
    protected autonomiaBateria: number;

    constructor(placa: string, ano: number, modelo: string, autonomiaBateria: number) {
        // Chama o construtor da classe pai
        super(placa, ano, modelo);
        this.autonomiaBateria = autonomiaBateria;
    }
}