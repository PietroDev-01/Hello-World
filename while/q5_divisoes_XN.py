#Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada 
#divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até 
#chegar a 2.

def main():
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Objetivo do programa: Lê 2 numeros, X e N e dividir até o numero n, sendo decrementado 1 em 1 a cada ciclo de calculo, chegar a 2.')
    numero_x = int(input('Digite um número(x): '))
    numero_n = int(input('Digite outro número(n): '))

    resultado_divisoes_xn = numero_x // numero_n
    contador = 1
    while numero_n > 1:
        
            resultado_divisoes_xn = numero_x // numero_n
            print(f'{contador} - A divisão entre {numero_x} e {numero_n} é {resultado_divisoes_xn}')
            numero_x  = resultado_divisoes_xn
            numero_n -= 1
            contador += 1

    print('FIM')

main()