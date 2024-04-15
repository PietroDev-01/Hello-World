#21. Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*) seja utilizado.

def main():
    print('                 --- Multiplique 2 números inteiros!!! ---')
    print('')
    numero1 = int(input('Insira o Primeiro número: '))
    numero2 = int(input('Insira o Segundo número: ')) - 1
    print('')
    acumulo = numero1
    numeroInicial = numero1
    if numero2 == -1 or numero1 == 0:
        numero1 = 0
        numero2 = 0
        print(f'    A multiplicação entre os números resulta em {numero1}')
    else:
        if numero1 > 0 and numero2 > 0: # 2 x 2
            while numero2 != 0:
                if numero2 == 0:
                    break
                if numero1 == 1:
                    numero1 = numero2 + 1
                    numero2 = 0
                    break
                numero1 += acumulo
                numero2 -= 1
            
            if numero2 == 0 or numero1 == 0:
                print(f'    A multiplicação entre os números resulta em {numero1}')

        elif numero1 < 0 and numero2 < 0: # -2 x -2
            while numero2 != 0:
                if numero2 == 0:
                    break
                if numero1 == -1:
                    numero1 = numero2 - 1
                    numero2 = 0
                    break
                numero1 -= acumulo
                numero2 += 1
            
            if numero2 == 0 or numero1 == 0:
                print(f'    A multiplicação entre os números resulta em {numero1}')

        elif numero1 > 0 and numero2 < 0: # 2 x -2
            while numero2 != 0:
                if numero2 == 0:
                    break
                if numero2 == -1:
                    numero1 = -numero1
                    numero2 = 0
                    break
                numero1 -= -acumulo
                numero2 += 1

            numero1 += numeroInicial

            if numero2 == 0 or numero1 == 0:
                print(f'    A multiplicação entre os números resulta em {numero1}')

        elif numero1 < 0 and numero2 > 0: # -2 x 2
            while numero2 != 0:
                if numero2 == 0:
                    break
                if numero2 == -1:
                    numero1 = -numero1
                    numero2 = 0
                    break
                numero1 += +acumulo
                numero2 -= 1
            
            if numero2 == 0 or numero1 == 0:
                print(f'    A multiplicação entre os números resulta em {numero1}')
    print('')


main()