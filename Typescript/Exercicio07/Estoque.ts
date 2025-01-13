class Produto {
    // adicionando atributos
    private identificador: number; 
    private descricao: string; 
    private quantidadeDeProdutosEmEstoque: number;  
    private valorUnitario: number; 

    // Construtor para inicializar os atributos
    constructor(identificador: number, descricao: string, quantidade: number, valor: number) {
        this.identificador = identificador;
        this.descricao = descricao;
        this.quantidadeDeProdutosEmEstoque = quantidade;
        this.valorUnitario = valor;
    }

    // Getters de atributos
    public getId(): number {
        return this.identificador;
    }
    public getDescricao(): string {
        return this.descricao;
    }
    public getQuantidade(): number {
        return this.quantidadeDeProdutosEmEstoque;
    }

    // Setter para atualizar a quantidade em estoque
    public setQuantidade(quantidade: number): void {
        this.quantidadeDeProdutosEmEstoque = quantidade;
    }

    // Método para repor produtos no estoque
    public repor(valor: number): string {
        this.quantidadeDeProdutosEmEstoque += valor; 
        return `Agora há ${this.quantidadeDeProdutosEmEstoque} produtos em estoque`;
    }

    // Método para dar baixa em produtos no estoque
    public darBaixa(valor: number): string {
        if (valor > this.quantidadeDeProdutosEmEstoque) {
            return "Quantidade insuficiente em estoque.";
        }
        this.quantidadeDeProdutosEmEstoque -= valor;
        return `Agora há ${this.quantidadeDeProdutosEmEstoque} produtos em estoque`;
    }
}


class ProdutoPerecivel extends Produto {
    private dataDeValidade: Date; // Data de validade do produto perecível

    // Construtor para inicializar os atributos de Produto e a data de validade
    constructor(identificador: number, descricao: string, quantidade: number, valor: number, validade: Date) {
        super(identificador, descricao, quantidade, valor); // Chamada ao construtor da classe base
        this.dataDeValidade = validade;
    }

    // Método para verificar se o produto está dentro da validade
    public verificarValidade(): boolean {
        return this.dataDeValidade >= new Date(); // Compara a data de validade com a data atual
    }

    // Sobrescrita do método repor para validar a data de validade antes de repor
    public override repor(valor: number): string {
        if (!this.verificarValidade()) {
            return "Operação não permitida: Produto fora da validade."; // Mensagem de erro se o produto estiver vencido
        }
        return super.repor(valor); // Chama o método original da classe base
    }

    // Sobrescrita do método dar baixa para validar a data de validade antes de executar
    public override darBaixa(valor: number): string {
        if (!this.verificarValidade()) {
            return "Operação não permitida: Produto fora da validade."; // Mensagem de erro se o produto estiver vencido
        }
        return super.darBaixa(valor); // Chama o método original da classe base
    }

    // Getter para acessar a data de validade
    public getValidade(): Date {
        return this.dataDeValidade;
    }
}


class Estoque {
    private produtos: (Produto | ProdutoPerecivel)[] = []; // Array para armazenar os produtos

    // Método para incluir um produto no estoque
    public incluir(produto: Produto | ProdutoPerecivel): string {
        if (this.existe(produto.getId(), produto.getDescricao())) { // Validação de duplicidade
            return "Produto com mesmo ID ou descrição já existe."; 
        }
        this.produtos.push(produto); // Adiciona o produto ao array
        return "Produto incluído com sucesso.";
    }

    // Método para excluir um produto do estoque pelo ID
    public excluir(id: number): string {
        for (let i = 0; i < this.produtos.length; i++) {// Busca o índice do produto
            if (this.produtos[i].getId() === id) {
                this.produtos.splice(i, 1); // Remove o produto do array
                return "Produto excluído com sucesso.";
            }
        }
        return "Produto não encontrado."; // Mensagem de erro se o produto não existir
    }

    // Método para consultar um produto pelo ID
    public consultar(id: number): Produto | ProdutoPerecivel | null { // retorna o produto ou null
        for (const produto of this.produtos) {
            if (produto.getId() === id) {
                return produto;
            }
        }
        return null;
    }

    // Método para verificar se um produto já existe pelo ID ou descrição
    public existe(id: number, descricao: string): boolean {
        return this.produtos.some(
            produto => produto.getId() === id || produto.getDescricao() === descricao
        ); // Retorna true se encontrar um produto com o mesmo ID ou descrição
    }

    // Método para repor a quantidade de um produto no estoque
    public repor(id: number, quantidade: number): string {
        const produto = this.consultar(id); // Consulta o produto pelo ID
        if (!produto) {
            return "Produto não encontrado."; // Mensagem de erro se o produto não existir
        }
        return produto.repor(quantidade); // Chama o método repor do produto
    }

    // Método para dar baixa na quantidade de um produto no estoque
    public darBaixa(id: number, quantidade: number): string {
        const produto = this.consultar(id); // Consulta o produto pelo ID
        if (!produto) {
            return "Produto não encontrado."; // Mensagem de erro se o produto não existir
        }
        return produto.darBaixa(quantidade); // Chama o método dar baixa do produto
    }

    // Método para listar todos os produtos perecíveis vencidos
    public listarPereciveisVencidos(): (ProdutoPerecivel)[] {
        return this.produtos
            .filter(produto => produto instanceof ProdutoPerecivel && !(produto as ProdutoPerecivel).verificarValidade())
            .map(produto => produto as ProdutoPerecivel); // Filtra e retorna apenas os produtos perecíveis vencidos
    }
}