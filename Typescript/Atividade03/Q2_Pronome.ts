function saudacao(nome: string, pronome: string = "Sr"): void {
    console.log(`${pronome}. ${nome}`);
}

saudacao("Sávia", "Sra"); // Sra. Sávia
saudacao("João");          // Sr. João
saudacao("Ocricrocrides"); // Sr. Ocricrocrides
saudacao("Zaradeia", "Sra"); // Sra. Zaradeia