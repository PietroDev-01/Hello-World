from ulid import ULID
import time
import os
import platform
# FUNÇÃO DE INSERIR MONTADORA

def insert_automaker():
    clear_screen()
    print('[1] Inserir Montadoras\n')

    #inputs
    name_automaker = input('Nome da Montadora: ').upper()
    country_automaker = input('País de Origem da Montadora: ').upper()
    year_of_fundation = int(input('Ano de Fundação da Montadora: '))
    id_automaker = ULID()

    print('\nA MONTADORA FOI CADASTRADA!\n')
    print('Redirecionando ao menu principal')

    # salvando montadora em arquivo
    with open('automaker_data.txt', 'a') as arquivo:
        montadoras_salvando = f'{id_automaker}#{name_automaker}#{country_automaker}#{year_of_fundation}'
        lista_a = [montadoras_salvando]

        #salvando a lista no  arquivo
        for item in lista_a:
            arquivo.write(item)
        arquivo.write('\n')
    

    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')

    clear_screen()

# FUNÇÃO DE LISTAR MONTADORAS
def list_automaker():
    clear_screen()
    print('[2] Listar Montadoras\n')
    print('Montadoras Cadastradas:\n')

    with open('automaker_data.txt', 'r') as arquivo_automaker:
        
        arquivo_lido = arquivo_automaker.readlines()
        montadoras = []  # Lista para armazenar os dados de cada montadora
        if not arquivo_lido:
            print('Por favor, insira pelo menos uma montadora primeiro.')
            enter = input('Aperte Enter para continuar! ')
            return
    
        for linha in arquivo_lido:
            linha = linha.strip()
            dados = linha.split('#')
            montadoras.append(dados)
        
        for montadora in montadoras:
            print(f'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
\033[33mId:\033[m {montadora[0]}
\033[33mNome:\033[m {montadora[1]}
\033[33mPaís de Origem:\033[m {montadora[2]}
\033[33mAno de Fundação:\033[m {montadora[3]}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')
    
        #lendo a quantidade de montadoras
        quantidade_de_montadoras = 0
        for _ in montadoras:
            quantidade_de_montadoras += 1
    print(f'Número de Montadoras Cadastradas: {quantidade_de_montadoras}')

    #Exibindo menu de filtragem e pedindo comando para o usuário
    print(list_automaker_filter())
    opcao = get_number_in_range('Expresse seu comando: ', 1, 4)

    if opcao == 1:
        remover_montadora(montadoras)
    elif opcao == 4:
        clear_screen()
        return



# FUNÇÕES

def remover_montadora(montadoras):
    remover_essa = input('Digite o Nome de qual montadora você quer remover: ').upper()

    montadoras_filtradas = []  # Lista para armazenar as montadoras que não serão removidas

    for montadora in montadoras:
        if montadora[1] != remover_essa:  # Se o nome da montadora for diferente, mantém
            montadoras_filtradas.append(montadora)
        else:
            print(f'Montadora {remover_essa} removida com sucesso.')

        montadoras = montadoras_filtradas
    
    enter = input('Aperte enter para continuar! ')
    # Salvando nova lista no arquivo sem a montadora
    lista_b = []
    with open('automaker_data.txt', 'w') as arquivo:
        
        for montadora in montadoras:
            montadoras_salvando_b = f'{montadora[0]}#{montadora[1]}#{montadora[2]}#{montadora[3]}'

            lista_b.append(montadoras_salvando_b + '\n')
        print(lista_b)
        #salvando a lista no  arquivo
        for item in lista_b:
            arquivo.write(str(item))
        #arquivo.write('\n')
        enter2 = input('Aperte enter para continuar! ')
        return

            

    
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

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# MENUS

def list_automaker_filter():
    menu = '''
[1] Remover Montadora
[2] Filtrar de A-Z (Em manutenção)
[3] Filtrar de Z-A (Em manutenção)
[4] Sair
'''
    return menu


def main_menu():
    os.system('cls')
    menu = print('''
[1] Inserir Montadoras (100%)
[2] Listar Montadoras (50%)
[3] Sair
''')
    return menu