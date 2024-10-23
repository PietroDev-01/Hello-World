import os

def criar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('Arquivo criado com sucesso!')
    print(f'Arquivo "{nome_arquivo}" criado com sucesso.')

def renomear_arquivo(nome_atual, novo_nome):
    if os.path.exists(nome_atual):
        os.rename(nome_atual, novo_nome)
        print(f'Arquivo renomeado para "{novo_nome}".')
    else:
        print(f'O arquivo "{nome_atual}" não existe.')

# Criando arquivo com nome padrão
nome_inicial = "Só alegria hahaha.txt"
criar_arquivo(nome_inicial)

# Solicitando novo nome
novo_nome = input('Digite o novo nome do arquivo (Use a extensão para criar um arquivo .txt): ')
renomear_arquivo(nome_inicial, novo_nome)