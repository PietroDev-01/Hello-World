# 1. Leia N e escreva todos os números inteiros de 1 a N.

def main():
    print('     Veja todos os numeros que estão entre 1 e seu número escolhido!!!')
    Numero = int(input('Número Inteiro Máximo escolhido: '))
    contadorN = 0

    for numero in range(2, Numero):
        contadorN += 1
        print(f'{contadorN}° - {numero}')
    print(f'Existem {contadorN} Números entre o número {Numero} e o número 1')

main()