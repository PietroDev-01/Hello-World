import utils

def main():
    utils.clear_screen()
    movies = []
    escolha = 1
    while escolha != 0:
        utils.show_menu()
        escolha = utils.get_number_in_range("Escolha: ", 0, 5)
        movies = executar(escolha, movies)


def executar(escolha, lista):
    if escolha == 1:
        new_movie = create_movie()
        lista.append(new_movie)
        print("Filme cadastrado com sucesso!")
    elif escolha == 2:
        listar_movies(lista)
    elif escolha == 3:
        lista = remover_movie(lista)
        print("Filme removido com sucesso!")
    elif escolha == 4:
        filtrar_filmes(lista)
    elif escolha == 5:
        salvar_em_arquivo(lista)

    utils.enter_to_continue()
    utils.clear_screen()
    return lista

# FUNÇÃO DE ADICIONAR FILMES

def create_movie():
    utils.clear_screen()
    print('1 - Cadastrar filme\n')
    movie = {}
    movie["nome"] = utils.get_text("Nome: ")
    movie["ano"] = utils.get_number("Ano de lançamento: ")
    movie["IMDB"] = float(input("Nota na IMDB: "))
    movie["bilheteria"] = utils.get_number("Arrecadação: ")
    return movie

# FUNÇÃO DE LISTAR FILMES

def listar_movies(movies):
    utils.clear_screen()
    print('2 - Listar filmes\n')
    for i, movie in enumerate(movies, 1):
        print(f"{i} - Nome: {movie['nome']} | Ano: {movie['ano']}")

# FUNÇÃO DE REMOVER FILMES

def remover_movie(movies):
    utils.clear_screen()
    listar_movies(movies)
    print('\nRemover um Filme da Lista\n')
    aux_movies = []
    escolha_remover = utils.get_number_in_range("Qual filme deseja remover? ", 1, len(movies))
    for i, movie in enumerate(movies, 1):
        if i == escolha_remover:
            continue
        aux_movies.append(movie)
    return aux_movies

# FUNÇÃO DE FILTRAGEM DOS FILMES

def filtrar_filmes(lista):
    utils.clear_screen()
    print('4 - Filtrar Filmes\n')

    # Garantindo com que a lista não venha vazia
    if not lista:
        print('Por favor, insira pelo menos um filme primeiro.')
        utils.enter_to_continue()
        return main()
    else:
        utils.show_filter()
        option = utils.get_number_in_range('Escolha: ', 1, 3)

        if option == 1:
            utils.filter_imdb(lista)
        elif option == 2:
            utils.filter_arrecadacao(lista)
        elif option == 3:
            utils.filter_years_movies(lista)
        
        return lista

# FUNÇÃO DE SALVAR ARQUIVO

def salvar_em_arquivo(lista):
    utils.clear_screen()
    print('4 - Salvar Filmes em arquivo\n')

    # Garantindo com que a lista não venha vazia
    if not lista:
        print('Por favor, insira pelo menos um filme primeiro.')
        utils.enter_to_continue()
        return main()
    else:
        print('-=-=-= Sua lista vai ser salva em um arquivo .txt -=-=-=\n')
        # pedindo nome do arquivo
        nome_do_arquivo = input('escolha o nome do arquivo [inclua o .txt no final]: ')
        # criando e inserindo lista (na verdade é um dicionário) no arquivo
        with open(f'{nome_do_arquivo}', 'w') as salvar_informacoes:
            for i in lista:
                salvar_informacoes.write(str(i) + '\n')
            print('\nLista salva com sucesso!')

main()