def main():
    print(menu)

    opcao = int(input('Escolha o método: '))

    if opcao == 1: 
        comprimento = int(input('Informe o comprimento da sequência fibonnaci desejado: '))
        comprimento_inicial = comprimento
        inicio = 0
        fibonnaci = 0
        n_anterior = 1
        n_sucessor = 1

        if comprimento_inicial < 1:
            print()
            print('Só é possível exibir a sequência fibonnaci se o comprimento for maior que 0 !')
            print()
        else:       
            while inicio < comprimento:

                if comprimento_inicial == 1:
                    print(0)
                    break
                elif comprimento_inicial == 2:
                    print(0)
                    print(1)
                    break

                if fibonnaci == 0:
                    print(0)
                    print(1)
                    print(1)
                    comprimento -= 3

                fibonnaci = n_anterior + n_sucessor
                n_anterior = n_sucessor
                n_sucessor = fibonnaci
                inicio += 1

                print(fibonnaci)
            print('...FIM...')
            

    if opcao == 2:
       comprimento = int(input('Informe o comprimento da sequência fibonnaci desejado: '))
       sequencia = []

       if comprimento < 1:
           print('\nSó é possível exibir a sequência fibonnaci se o comprimento for maior que 0 !!')
       elif comprimento == 1:
            sequencia = [0]
       elif comprimento == 2:
                sequencia = [0, 1]
       else:
                sequencia = [0, 1]
                for i in range(2, comprimento):
                 proximo_numero = sequencia[-1] + sequencia[-2]
                 sequencia.append(proximo_numero)                
        
       if comprimento < 1:
           print()
       else:
        print(sequencia)
           
        

    if opcao == 3:
        comprimento = int(input('Informe o comprimento da sequência fibonnaci desejado: '))

        def funcao_fibonnaci(n):
            if n < 1:
                return 'Só é possível exibir a sequência fibonnaci se o comprimento for maior que 0 !!!'
            elif n == 1:
                return [0]
            elif n == 2:
                return [0, 1]
            else:
                sequencia = funcao_fibonnaci(n - 1)
                sequencia.append(sequencia[-1] + sequencia[-2])
                return sequencia 
        
        sequencia = funcao_fibonnaci(comprimento)
        print(f'\nSequencia Fibonnaci >>> {sequencia}\n')
       
        
    if opcao > 3 or opcao < 1:
        if opcao == 4:
            print('\nObrigado pelo seu tempo :)')
        print('Fim\n')



menu = '''
[1] Fibonnaci por While
[2] Fibonnaci por For
[3] Fibonnaci por Recursividade
[4] Sair'''

main()