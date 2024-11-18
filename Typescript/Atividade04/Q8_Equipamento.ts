/*8. Uma classe Equipamento com:
a. um atributo ligado (tipo boolean)
b. dois métodos liga() e desliga(). O método liga torna o atributo ligado true e
o método desliga torna o atributo ligado false.
c. Crie um método chamado inverte(), que muda o status atual (se ligado,
desliga...se desligado, liga)
d. Crie um método que estaLigado() que retorna o valor do atributo ligado
e. Altere o comportamento do método ligar() para caso o equipamento já
esteja ligado, não ligue novamente. Faça o mesmo com o método
desligar().
f. Instancie uma classe Equipamento e teste todos os seus métodos.
*/

class Equipamento {
    ligado: boolean;

    liga(): void{
        if (this.ligado == true){
            this.ligado = this.ligado;
            console.log("Já está Ligado!");
        } else {
            this.ligado = true;
            console.log("Ligado!");
        }
    }
    desliga(): void{
        if (this.ligado == false){
            this.ligado = this.ligado;
            console.log("Já Está Desligado!");
        } else {
            this.ligado = false;
            console.log("Desligado!");
        }
    }
    inverte(): void{
        if (this.ligado == true){
            this.ligado = false;
            console.log("Agora está Desligado!");
        }
        if (this.ligado == false){
            this.ligado = true;
            console.log("Agora está Ligado!");
        }
    }
    estaLigado(): void{
        console.log(this.ligado);
    }
}

let testeEquipamento: Equipamento = new Equipamento();
testeEquipamento.liga() // Ligado!
testeEquipamento.desliga() // Desligado!
testeEquipamento.inverte() // Agora está desligado!
testeEquipamento.estaLigado() // True