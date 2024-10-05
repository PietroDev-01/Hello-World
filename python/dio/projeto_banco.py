import time
import platform
import os
def main(saldo=0, extrato_deposito='', extrato_saque='', numeroDeSaques=0):
    clear_screen()
    menu = main_menu()
    print(menu)
    opcao = input(('Faça sua escolha: '))

    limite = 500
    LIMITEDESAQUES = 3
        
    # FUNÇÃO DE DEPÓSITO
    if opcao.upper() == 'D':
        clear_screen()
        print('DEPÓSITO')
        valor_de_deposito = -1
        while valor_de_deposito < 0:
            valor_de_deposito = int(input('Valor para depósito: R$ '))

            if valor_de_deposito < 0:
                print('\033[33mAVISO:\033[mPor favor insira uma quantia válida para depósito!')
                

        extrato_deposito += f'Depósito realizado de : R$ {valor_de_deposito}\n'
        saldo = saldo + valor_de_deposito
        print(f'Depósito realizado de : R$ {valor_de_deposito}')
        enter = input('Aperte enter para voltar ao menu! ')
        clear_screen()
        return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)
    
    # FUNÇÃO DE SAQUE

    elif opcao.upper() == 'S':
        clear_screen()
        if numeroDeSaques == LIMITEDESAQUES:
            print('\033[33mAVISO:\033[m Limite de saques diários atingido!')
            enter = input('Aperte enter para voltar ao menu! ')
            clear_screen()
            return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)
        
        print('SACAR')

        while numeroDeSaques != LIMITEDESAQUES:
            if saldo == 0:
                print('\033[33mAVISO:\033[m Você não tem saldo para realizar um saque!')
                enter = input('Aperte enter para voltar ao menu! ')
                return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)

            valor_de_saque = int(input('Insira o valor de saque: ' ))

            if valor_de_saque > saldo:
                print(f'\033[33mAVISO:\033[m Saque não realizado pois o valor em conta (R${saldo}) é menor que o valor do saque (R${valor_de_saque})')
                enter = input('Aperte enter para voltar ao menu! ')
                clear_screen()
                return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)
                
            elif valor_de_saque > limite:
                print(f'\033[33mAVISO:\033[m Saque não realizado pois o valor limite de saque (R${limite}) é menor que o valor requisitado (R${valor_de_saque})')
                enter = input('Aperte enter para voltar ao menu! ')
                clear_screen()
                return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)
                
            else:
                saldo -= valor_de_saque
                print('\033[33mSaque realizado com sucesso!\033[m')
                enter = input('Aperte enter para voltar ao menu! ')
                extrato_saque += f'Saque realizado de : R$ {valor_de_saque}\n'
                numeroDeSaques += 1

                clear_screen()
                return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)   

    # FUNÇÃO PARA EXIBIR O EXTRATO

    elif opcao.upper() == 'E':
        clear_screen()
        print('EXTRATO:')

        extrato = print(f'''
\033[33m-=-=-=-=-=-= Extrato Depósitos =-=-=-=-=-=-\033[m
{extrato_deposito}

\033[33m-=-=-=-=-=-= Extrato Saques =-=-=-=-=-=-\033[m
{extrato_saque}

\033[33m-=-=-=-=-=-= Saldo =-=-=-=-=-=-\033[m
{saldo}
''')
        enter = input('Aperte enter para voltar ao menu! ')
        clear_screen()
        return main(saldo, extrato_deposito, extrato_saque, numeroDeSaques)
    
    # FUNÇÃO DE SAIR DO PROGRAMA

    elif opcao.upper() == 'Q':
        clear_screen()
        print('\033[33mVolte sempre!\033[m')
        time.sleep(3)
        clear_screen()

# FUNÇÕES AUXILIARES

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

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

def main_menu():
    print('''
[D] DEPOSITAR
[S] SACAR
[E] EXTRATO
[Q] SAIR
''')


main()