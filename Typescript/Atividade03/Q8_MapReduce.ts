const array = [1, 2, 3, 4, 5];

// Dobrar os elementos usando map
const dobrados = array.map(numero => numero * 2);

// Somar todos os elementos usando reduce
const somaTotal = dobrados.reduce((acumulador, numero) => acumulador + numero, 0);

console.log(dobrados);  // Saída: [2, 4, 6, 8, 10]
console.log(somaTotal); // Saída: 30
