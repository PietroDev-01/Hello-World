class Retangulo {
    l1: number = 0;
    l2: number = 0;

    calcularArea(): number {
        return this.l1 * this.l2;
    }

    calcularPerimetro(): number {
        return 2 * (this.l1 + this.l2);
    }

    isQuadrado(): boolean {
        return this.l1 === this.l2; // Retorna verdadeiro se l1 e l2 forem iguais
    }
}

let r1: Retangulo = new Retangulo();
r1.l1 = 3;
r1.l2 = 3;

console.log("Área: " + r1.calcularArea());
console.log("Perímetro: " + r1.calcularPerimetro());
console.log("É um quadrado? " + r1.isQuadrado());
