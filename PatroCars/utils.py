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

    print('\n\033[33mA MONTADORA FOI CADASTRADA!\033[m\n')
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
    opcao = get_number_in_range('Expresse seu comando: ', 1, 6)

    if opcao == 1:
        remover_montadora(montadoras)
    elif opcao == 2:
        filtrar_montadoras_AZ(montadoras)
    elif opcao == 3:
        filtrar_montadoras_ZA(montadoras)
    elif opcao == 4:
        filtrar_montadoras_novo_para_antigo(montadoras)
    elif opcao == 5:
        filtrar_montadoras_antigo_para_novo(montadoras)
    elif opcao == 6:
        clear_screen()
        return


# FUNÇÕES DERIVADAS DA LISTAR MONTADORAS (1 função é base de outras 3 funções)


def remover_montadora(montadoras):
    remover_essa = input('Digite o Nome de qual montadora você quer remover: ').upper()

    montadoras_filtradas = []  # Lista para armazenar as montadoras que não serão removidas

    for montadora in montadoras:
        if montadora[1] != remover_essa:  # Se o nome da montadora for diferente, mantém
            montadoras_filtradas.append(montadora)
        else:
            print(f'Montadora {remover_essa} removida com sucesso.')

        montadoras = montadoras_filtradas
    
    # Salvando nova lista no arquivo sem a montadora
    lista_b = []
    with open('automaker_data.txt', 'w') as arquivo:
        
        for montadora in montadoras:
            montadoras_salvando_b = f'{montadora[0]}#{montadora[1]}#{montadora[2]}#{montadora[3]}'

            lista_b.append(montadoras_salvando_b + '\n')
        
        #salvando a lista no  arquivo
        for item in lista_b:
            arquivo.write(str(item))

        enter2 = input('Aperte enter para continuar! ')
        return
            
def filtrar_montadoras_AZ(montadoras):

    # DARIA PRA METER UM IF DE VERIFICAÇÃO AQUI VIU (SÓ NÃO SEI COMO, AINDA)
    
    lista_com_dicionarios = []
    for montadora in montadoras: # Convertendo de lista para dicionarios
        dicionario_montadora = {'ID': montadora[0], 'Nome': montadora[1], 'País': montadora[2], 'Ano': montadora[3]}
        lista_com_dicionarios.append(dicionario_montadora)
    
    montadoras_ordenadas = sorted(lista_com_dicionarios, key=lambda x: x['Nome']) # Ordenando de A-Z
    lista_c = [] # Lista para colocar os dicionarios com as montadoras ordenadas
    for item in montadoras_ordenadas: # percorrendo cada dicionario e convertendo em strings simples para salvar em arquivo
        salvando_arquivo_ordenados_AZ = f'{item['ID']}#{item['Nome']}#{item['País']}#{item['Ano']}'
        lista_c.append(salvando_arquivo_ordenados_AZ)


    with open('automaker_data.txt', 'w') as arquivo:
        #salvando a lista no  arquivo
        for montadora in lista_c:
            arquivo.write(montadora + '\n')
    
    print('\033[33mAVISO:\033[m O arquivo foi salvo ordenadamente de A-Z, recarregue a página para visualizar!')
    enter3 = input('Aperte enter para continuar! ')
    return

def filtrar_montadoras_ZA(montadoras): # IMPORTANTE: O CÓDIGO É O MESMO DE A-Z, SÓ ADICIONEI O REVERSE = TRUE NO SORTED !!!

    lista_com_dicionarios = []
    for montadora in montadoras: # Convertendo de lista para dicionarios
        dicionario_montadora = {'ID': montadora[0], 'Nome': montadora[1], 'País': montadora[2], 'Ano': montadora[3]}
        lista_com_dicionarios.append(dicionario_montadora)
    
    montadoras_ordenadas = sorted(lista_com_dicionarios, key=lambda x: x['Nome'], reverse = True) # Ordenando de Z-A
    lista_c = [] # Lista para colocar os dicionarios com as montadoras ordenadas
    for item in montadoras_ordenadas: # percorrendo cada dicionario e convertendo em strings simples para salvar em arquivo
        salvando_arquivo_ordenados_AZ = f'{item['ID']}#{item['Nome']}#{item['País']}#{item['Ano']}'
        lista_c.append(salvando_arquivo_ordenados_AZ)


    with open('automaker_data.txt', 'w') as arquivo:
        #salvando a lista no  arquivo
        for montadora in lista_c:
            arquivo.write(montadora + '\n')
    
    print('\033[33mAVISO:\033[m O arquivo foi salvo ordenadamente de Z-A, recarregue a página para visualizar!')
    enter3 = input('Aperte enter para continuar! ')
    return

def filtrar_montadoras_novo_para_antigo(montadoras): # IMPORTANTE: O CÓDIGO É O MESMO DE A-Z, SÓ TROQUEI A CHAVE E ADICIONEI O REVERSE = TRUE NO SORTED !!!

    lista_com_dicionarios = []
    for montadora in montadoras: # Convertendo de lista para dicionarios
        dicionario_montadora = {'ID': montadora[0], 'Nome': montadora[1], 'País': montadora[2], 'Ano': montadora[3]}
        lista_com_dicionarios.append(dicionario_montadora)
    
    montadoras_ordenadas = sorted(lista_com_dicionarios, key=lambda x: x['Ano'], reverse = True) # Ordenando do mais novo para o mais antigo
    lista_c = [] # Lista para colocar os dicionarios com as montadoras ordenadas
    for item in montadoras_ordenadas: # percorrendo cada dicionario e convertendo em strings simples para salvar em arquivo
        salvando_arquivo_ordenados_AZ = f'{item['ID']}#{item['Nome']}#{item['País']}#{item['Ano']}'
        lista_c.append(salvando_arquivo_ordenados_AZ)


    with open('automaker_data.txt', 'w') as arquivo:
        #salvando a lista no  arquivo
        for montadora in lista_c:
            arquivo.write(montadora + '\n')
    
    print('\033[33mAVISO:\033[m O arquivo foi salvo ordenadamente da montadora mais antiga para a mais nova, recarregue a página para visualizar!')
    enter3 = input('Aperte enter para continuar! ')
    return
    
def filtrar_montadoras_antigo_para_novo(montadoras): # IMPORTANTE: O CÓDIGO É O MESMO DE A-Z, SÓ TROQUEI A CHAVE E ADICIONEI O REVERSE = FALSE NO SORTED !!!

    lista_com_dicionarios = []
    for montadora in montadoras: # Convertendo de lista para dicionarios
        dicionario_montadora = {'ID': montadora[0], 'Nome': montadora[1], 'País': montadora[2], 'Ano': montadora[3]}
        lista_com_dicionarios.append(dicionario_montadora)
    
    montadoras_ordenadas = sorted(lista_com_dicionarios, key=lambda x: x['Ano']) # Ordenando do mais antigo para o mais novo
    lista_c = [] # Lista para colocar os dicionarios com as montadoras ordenadas
    for item in montadoras_ordenadas: # percorrendo cada dicionario e convertendo em strings simples para salvar em arquivo
        salvando_arquivo_ordenados_AZ = f'{item['ID']}#{item['Nome']}#{item['País']}#{item['Ano']}'
        lista_c.append(salvando_arquivo_ordenados_AZ)


    with open('automaker_data.txt', 'w') as arquivo:
        #salvando a lista no  arquivo
        for montadora in lista_c:
            arquivo.write(montadora + '\n')
    
    print('\033[33mAVISO:\033[m O arquivo foi salvo ordenadamente da montadora mais nova para a mais antiga, recarregue a página para visualizar!')
    enter3 = input('Aperte enter para continuar! ')

# FUNÇÕES SIMPLES

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
[2] Filtrar de A-Z (100%)
[3] Filtrar de Z-A (100%)
[4] Filtrar por ano de Fundação (Mais novo ao Mais antigo) (100%)
[5] Filtrar por ano de Fundação (Mais antigo ao Mais novo) (100%)
[6] Sair
'''
    return menu


def main_menu():
    os.system('cls')
    menu = print('''
[1] Inserir Montadoras (100%)
[2] Listar Montadoras (100%)
[3] Sair
''')
    return menu