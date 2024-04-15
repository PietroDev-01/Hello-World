#5. Leia um número, calcule e escreva seu fatorial.

def main():
    print('                                 !!! Descubra qual o fatorial de um número Natural!!!')
    print('')
    numeroFatorial = int(input('Número para ser fatorado: '))
    numeroInicial = numeroFatorial
    colecaoFatorial = []
    contadorvezes = numeroFatorial
    contadorvezes2 = numeroFatorial
    if numeroInicial < 0:
        print('!!! Insira um número Natural positivo !!!')
    elif numeroInicial != 0 and numeroInicial != 1:
        print(f'O fatorial de {numeroFatorial}! é: ')
    elif numeroInicial == 0:
        print('0! Fatorial corresponde a 1')
    elif numeroInicial == 1:
        print('1! Fatorial corresponde a 1')
    while contadorvezes > 0:
        if contadorvezes == 0:
            break
        contadorvezes -= 1
        numeroFatorial *= contadorvezes
        colecaoFatorial.append(numeroFatorial)

    for fatorial in colecaoFatorial:
        contadorvezes2 -= 1
        if contadorvezes2 == 0:
            print('                                                                        FIM')
            break
        else:
            print(f'{numeroInicial} x {contadorvezes2} = {fatorial}')
            numeroInicial = fatorial
    print('')

main()
    