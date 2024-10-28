/*

5. Crie uma classe chamada ControleDeAudio a partir das orientações:
a. A classe deve ter um atributo inteiro representando o volume inicializado
com o valor 2.
b. Crie um método chamado aumentar volume que incrementa em um o
valor atual. O método não deve deixar o valor ficar maior que 10. Utilize
um if para isso;
c. Crie um método chamado diminuir volume que decrementa em um o
valor atual. O método não deve deixar o valor ficar menor 0.
d. Crie um método chamado lerVolume que retorna o valor do volume.

**/

class ControleDeAudio{
    volume: number = 0;

    AumentarVolume(): number {
        if (this.volume > 10){
            return this.volume = 10;
        }
        else{
            return this.volume += 1;
        }
    }

    DiminuirVolume(): number {
        if (this.volume < 0){
            return this.volume = 0;
        }
        else{
            return this.volume -= 1;
        }
    }

    LerVolume(): number {
        return this.volume;
    }

}

let controle: ControleDeAudio = new ControleDeAudio();
controle.volume = 2;


console.log("Volume aumentado para: " + controle.AumentarVolume());
console.log("Volume diminuido para: " + controle.DiminuirVolume());
console.log("Volume agora: " + controle.LerVolume());
