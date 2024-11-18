/*7. Crie uma classe chamada Triangulo que:
• Possua 3 atributos inteiros representando os lados;
• Crie um método que retorna true se os lados formarem um triângulo de
acordo com a regra: |b-c| < a < b+c;
• Crie 3 métodos: ehIsoceles(), ehEquilatero() e ehEscaleno() que retorne
verdadeiro caso o triângulo seja um dos tipos relacionados ao nome do
método. Eles devem chamar antes de tudo, o método da questão b. e
retornar false se esse método já retornar false também;
• Instancie classes Triangulo de diferentes lados e seus métodos.
*/

class Triangulo {
    lado1: number = 0;
    lado2: number = 0;
    lado3: number = 0;

    FormaTriangulo(): boolean{
        if ((this.lado2 - this.lado3 < this.lado1) && (this.lado1 < this.lado2 + this.lado3)){
            return true
        } else {
            return false
        }

    }

    ehIsosceles(): void{
        if (this.FormaTriangulo() == true){
            if (this.lado1 == this.lado2 || this.lado2 == this.lado3){
                return console.log("É isosceles!");
            } else {
                return console.log("Não é isosceles!");
            }
        } else {
            return console.log("Não Forma triangulo!");
        }
    }

    ehEquilatero(): void{
        if (this.FormaTriangulo() == true){
            if (this.lado1 == this.lado2 && this.lado2 == this.lado3){
                return console.log("É Equilatero!");
            } else {
                return console.log("Não é Equilatero!");
            }
        } else {
            return console.log("Não Forma triangulo!");
        }
    }

    ehEscaleno(): void{
        if (this.FormaTriangulo() == true){
            if (this.lado1 != this.lado2 && this.lado2 != this.lado3){
                return console.log("É Escaleno!");
            } else {
                return console.log("Não é Escaleno!");
            }
        } else {
            return console.log("Não Forma triangulo!");
        }
    }
}

let testetriangulo: Triangulo = new Triangulo();
testetriangulo.lado1 = 5
testetriangulo.lado2 = 5
testetriangulo.lado3 = 5

testetriangulo.ehIsosceles() // É isosceles!
testetriangulo.ehEquilatero() // É Equilatero!
testetriangulo.ehEscaleno() // É Escaleno!