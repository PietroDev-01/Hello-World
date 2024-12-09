/**2. Crie uma implementação que simule um migroblog:
a. Crie uma classe Postagem e nela:
a. Crie os atributos:
1. id do tipo number, representando o identificador da
postagem;
2. texto do tipo string, representando um texto da postagem;
3. quantidadeCurtidas do tipo number;
b. Crie um método chamado curtir que incrementa a quantidade
curtidas;
c. Crie um método chamado toString que retorna a concatenação da
postagem com a quantidade de curtidas;

b. Crie uma classe Microblog e nela:
a. Crie um array de classes Postagem;
b. Crie um método que inclua uma postagem passada como
parâmetro no array de postagens;
c. Crie um método de excluir uma postagem que recebe um id
passado por parâmetro. Para isso, efetue uma busca pelo id nas
postagens do array e faça a exclusão de forma análoga à feita na
classe Banco;
d. Crie um método que retorna a postagem mais curtida;
e. Crie um método curtir em que se passa um id como parâmetro e a
classe microblog pesquisa a postagem e chama seu método curtir
da própria postagem;

f. Crie um método toString que retorna a concatenação do “toString”
de todas as postagens. */

class Postagem {
    id: number;
    texto: string;
    quantidadeCurtidas: number;

    constructor(id: number, texto: string) {
        this.id = id;
        this.texto = texto;
        this.quantidadeCurtidas = 0;
    }

    curtir(): void {
        this.quantidadeCurtidas++;
    }

    toString(): string {
        return `Postagem [ID: ${this.id}, Texto: "${this.texto}", Curtidas: ${this.quantidadeCurtidas}]`;
    }
}

class Microblog {
    postagens: Postagem[];

    constructor() {
        this.postagens = [];
    }

    adicionarPostagem(postagem: Postagem): void {
        this.postagens.push(postagem);
    }

    excluirPostagem(id: number): void {
        const index = this.postagens.findIndex(post => post.id === id);
        if (index === -1) {
            throw new Error("Postagem não encontrada.");
        }
        this.postagens.splice(index, 1);
    }

    postagemMaisCurtida(): Postagem | null {
        if (this.postagens.length === 0) return null;
        return this.postagens.reduce((maisCurtida, postagemAtual) =>
            postagemAtual.quantidadeCurtidas > maisCurtida.quantidadeCurtidas
                ? postagemAtual
                : maisCurtida
        );
    }

    curtirPostagem(id: number): void {
        const postagem = this.postagens.find(post => post.id === id);
        if (!postagem) {
            throw new Error("Postagem não encontrada.");
        }
        postagem.curtir();
    }
}

// Testando as classes
const microblog = new Microblog();

const postagem1 = new Postagem(1, "Primeira postagem!");
const postagem2 = new Postagem(2, "Segunda postagem!");
const postagem3 = new Postagem(3, "Mais uma postagem interessante!");

microblog.adicionarPostagem(postagem1);
microblog.adicionarPostagem(postagem2);
microblog.adicionarPostagem(postagem3);

console.log("Postagens iniciais:");
microblog.postagens.forEach(post => console.log(post.toString()));

microblog.curtirPostagem(1);
microblog.curtirPostagem(1);
microblog.curtirPostagem(2);

console.log("\nPostagens após curtidas:");
microblog.postagens.forEach(post => console.log(post.toString()));

console.log("\nPostagem mais curtida:");
const maisCurtida = microblog.postagemMaisCurtida();
console.log(maisCurtida ? maisCurtida.toString() : "Nenhuma postagem encontrada.");

microblog.excluirPostagem(2);
console.log("\nPostagens após exclusão:");
microblog.postagens.forEach(post => console.log(post.toString()));
