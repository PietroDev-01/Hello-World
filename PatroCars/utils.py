from ulid import ULID
import time
import os

def insert_automaker():
    os.system('cls')
    print('[1] Inserir Montadoras\n')

    #inputs
    name_automaker = input('Nome da Montadora: ')
    country_automaker = input('País de Origem da Montadora: ')
    year_of_fundation = int(input('Ano de Fundação da Montadora: '))
    id_automaker = ULID()

    print('\nA MONTADORA FOI CADASTRADA!\n')
    print('Redirecionando ao menu principal')
    # Colocando inputs em dicionario e inserindo dicionario em uma lista
    with open('automaker_data.txt', 'a') as arquivo:
        dicionario = {"ID": str(id_automaker), "Nome da Montadora": name_automaker, "Nacionalidade da Montadora": country_automaker, "Ano de Fundação da Montadora": year_of_fundation}
        lista_a = [dicionario]

        #salvando a lista no  arquivo
        for item in lista_a:
            arquivo.write(str(item) + ' ')
        arquivo.write('\n')
    

    time.sleep(1.25)
    print('...')
    time.sleep(1.25)
    print('...')
    time.sleep(1)
    print('...')

    os.system('cls')


def list_automaker():
    os.system('cls')
    print('[2] Listar Montadoras\n')
    print('Montadoras Cadastradas:')

    with open('automaker_data.txt', 'r') as arquivo_automaker:
        arquivo_lido = arquivo_automaker.read()
        # Exibindo tudo que há na lista
        print(arquivo_lido)
    
        #lendo a quantidade de montadoras
        quantidade_de_montadoras = 0
        for linha in arquivo_lido:
            if linha == '\n':
                quantidade_de_montadoras += 1

    print(f'Número de Montadoras Cadastradas: {quantidade_de_montadoras}')
    #Exibindo menu de filtragem e pedindo comando para o usuário
    print(list_automaker_filter())
    opcao = int(input('Expresse seu comando: '))

    if opcao == 99:
        os.system('cls')
        return
    elif opcao == 1:
        remover_montadora()


# FUNÇÕES

def remover_montadora():
    os.system('cls')
    print('')
    

# MENUS

def list_automaker_filter():
    menu = '''
[1] Filtrar de A-Z (Em manutenção)
[2] Filtrar de Z-A (Em manutenção)
[99] Sair
'''
    return menu


def main_menu():
    os.system('cls')
    menu = print('''
[1] Inserir Montadoras (100%)
[2] Listar Montadoras (50%)
[3] Remover Montadoras (Desenvolvendo)
[99] Sair
''')
    return menu