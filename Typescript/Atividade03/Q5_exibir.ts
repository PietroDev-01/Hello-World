function exibir(...elementos: string[]): void {
    elementos.forEach(elemento => console.log(elemento));
}

exibir("a", "b");
// Saída:
// a
// b
exibir("a", "b", "c");
// Saída:
// a
// b
// c
exibir("a", "b", "c", "d");
// Saída:
// a
// b
// c
// d