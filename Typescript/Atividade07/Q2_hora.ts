/*
2. Crie uma classe Hora que tenha:
a. Três atributos privados e definidos no construtor chamados hora, minutos e
segundos;
b. Métodos públicos para ler hora, minuto e segundo de forma individual;
c. Um método público para retorne a hora no formato “hh:mm:ss”.*/

class Hora{
    private hora: number;
    private minutos: number;
    private segundos: number;

    constructor(hora: number, minutos: number, segundos: number){
        this.hora = hora;
        this.minutos = minutos;
        this.segundos = segundos;
    }
    
    
    public lerHora(): number{
        return this.hora;
    }
    
    public lerMinutos(): number{
        return this.minutos;
    }
    
    public lerSegundos(): number{
        return this.segundos;
    }
    public exibirHora(): string{
        return `${this.hora}:${this.minutos}:${this.segundos}`;
    }
}

var relogio = new Hora(22, 43, 50);

console.log(`Hora: ${relogio.lerHora()}`)
console.log(`Minutos: ${relogio.lerMinutos()}`)
console.log(`Segundos: ${relogio.lerSegundos()}`)
console.log(`Rádio FM informa a hora certa: ${relogio.exibirHora()}`);