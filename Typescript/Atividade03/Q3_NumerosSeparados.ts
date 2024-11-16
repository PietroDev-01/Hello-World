function numerosSeparados(numeros: number[]): string {
    let resultado = "";
    numeros.forEach((numero, index) => {
      resultado += numero;
      if (index < numeros.length - 1) {
        resultado += "-";
      }
    });
    return resultado;
}

console.log(numerosSeparados([1, 2, 3, 4])); // "1-2-3-4"
console.log(numerosSeparados([10, 20, 30])); // "10-20-30"