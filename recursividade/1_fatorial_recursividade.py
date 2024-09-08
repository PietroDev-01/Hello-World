# Calcule o fatorial de um número

def main():

    print(menu)

    opcao = int(input('Escolha o método: '))

    if opcao == 1: 
        fatorial = int(input('\nDigite o número que deseja fatorar: '))
        numero_para_print = fatorial
        resultado = fatorial

        if fatorial == 1 or fatorial == 0:
            print(f'\nO fatorial de {numero_para_print} é 1\n')
        elif fatorial < 0 :
            print('\nSó pode-se obter fatorial de números positivos!\n')
        else:
            while fatorial != 1:
                resultado = resultado * (fatorial - 1)
                fatorial -= 1

            print(f'\nO fatorial de {numero_para_print} é {resultado} !\n')

    if opcao == 2:
        fatorial = int(input('\nDigite o número que deseja fatorar: '))
        n = 1
        
        if fatorial < 0:
            print('\nSó pode-se obter fatorial de números positivos!\n')
        else:
            for i in range(1, fatorial + 1):
                n *= i

            print(f'\no fatorial de {fatorial} é {n} !!\n')

        

    if opcao == 3:
        fatorial = int(input('\nDigite o número que deseja fatorar: ')) 
        
        def funcao_fatorial(n):
                if n == 0 or n == 1:
                    return 1
                
                return n * funcao_fatorial(n - 1)
                
        funcao = funcao_fatorial(fatorial)
        print(f'\nO fatorial de {fatorial} é {funcao} !!!\n')
        
    if opcao > 3 or opcao < 1:
        if opcao == 4:
            print('\nObrigado pelo seu tempo :)')
        print('Fim\n')


menu = '''
[1] Fatoração por While
[2] Fatoração por For
[3] Fatoração por Recursividade
[4] Sair'''

main()