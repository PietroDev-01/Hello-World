#3. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão  Aritmética que tem por valor inicial A0 e razão R.

def main():
    print('                                         !!! Crie sua própria Progressão Aritmética !!!')
    print('')
    numeroinicial = int(input('Insira o Número inical da Progressão Aritmética: '))
    razaoPA = int(input('Escreva a Razão da sua Progressão Aritmética: '))
    limitePA = int(input('Insira o limite da sua Progressão Aritmética: '))
    print('')
    contadorNumeros = 0
    if numeroinicial > limitePA and razaoPA > 0:
        print('Ajuste o limite da sua PA, para que fique maior que seu número inicial, ou considere inserir uma razão negativa')
    elif razaoPA == 0:
        print(f'Essa PA é infinita e possui todos os termos iguais a "{numeroinicial}", Decorrente da sua Razão = 0')
    elif numeroinicial == limitePA:
        print('Considere não igualar o valor inicial ao valor limite para assim fazer uma PA real')
    elif numeroinicial < 0 and razaoPA < 0 and limitePA > 0 or numeroinicial > 0 and razaoPA < 0 and limitePA > 0:
        print('Reajuste seu limite para negativo ou sua razão para positiva, assim é possível obter uma PA coerente')
    else:
        for PA in range(numeroinicial, limitePA, razaoPA):
            contadorNumeros += 1
            print(f'                Termo A{contadorNumeros} da PA: {PA}')
    print('')
main()