import os
import platform

def get_text(prompt):
    return input(prompt)


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, insira um número válido.")

def get_number_in_range(prompt, min_value, max_value):
    while True:
        num = get_number(prompt)
        if min_value <= num <= max_value:
            return num
        print(f"Escolha um número entre {min_value} e {max_value}.")

    
def enter_to_continue():
    input("Pressione Enter para continuar... ")

    
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# FUNÇÕES DE FILTRAGEM

def filter_imdb(lista):
    # Ordena a lista pelo campo 'IMDB' e pega o menor e o maior
    movie_with_highest_imdb = max(lista, key=lambda x: x['IMDB'])
    movie_with_lowest_imdb = min(lista, key=lambda x: x['IMDB'])

    print(f"Filme com maior nota IMDB: {movie_with_highest_imdb['nome']} - Nota: {movie_with_highest_imdb['IMDB']}")
    print(f"Filme com menor nota IMDB: {movie_with_lowest_imdb['nome']} - Nota: {movie_with_lowest_imdb['IMDB']}")

def filter_arrecadacao(lista):
    # Ordena a lista pelo campo 'bilheteria' e pega o menor e o maior
    movie_with_highest_bilheteria = max(lista, key=lambda x: x['bilheteria'])
    movie_with_lowest_bilheteria = min(lista, key=lambda x: x['bilheteria'])

    print(f"Filme com maior arrecadação: {movie_with_highest_bilheteria['nome']} - Arrecadação: {movie_with_highest_bilheteria['bilheteria']}")
    print(f"Filme com menor arrecadação: {movie_with_lowest_bilheteria['nome']} - Arrecadação: {movie_with_lowest_bilheteria['bilheteria']}")

def filter_years_movies(lista):
    # Ordena a lista pelo campo 'ano' e pega o mais antigo e o mais novo
    movie_with_most_recent_year = max(lista, key=lambda x: x['ano'])
    movie_with_oldest_year = min(lista, key=lambda x: x['ano'])

    print(f"Filme mais recente: {movie_with_most_recent_year['nome']} - Ano: {movie_with_most_recent_year['ano']}")
    print(f"Filme mais antigo: {movie_with_oldest_year['nome']} - Ano: {movie_with_oldest_year['ano']}")

# MENUS

def show_menu():
    print("""
    -=-=-=-= ROGER CINE =-=-=-=-
    1 - Cadastrar filme
    2 - Listar filmes
    3 - Remover um filme da lista
    4 - Filtrar Filmes
    5 - Salvar Filmes em arquivo
    
    0 - Sair
    """)

def show_filter():
    print('''
1 - Filmes com maior e menor nota IMDB
2 - Filmes com maior e menor arrecadação
3 - Filmes mais novos e mais antigos da lista''')
