# Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária e na base hexadecimal.

def main ():
    print('Conversor de: decimal para: binário e hexadecimal')
    numero = int(input('Número de base decimal entre 0 e 255: '))
    numero_bin = numero
    numero_hex = numero
    divisor = 0
    contador = 1
    print(f'{numero} na base binária: ')
    binario = ''
    while numero_bin != 0:
        if numero > 255:
            print('Apenas números entre 0 e 255 são aceitos')
            break
        divisor = numero_bin // 2
        resto = numero_bin % 2
        binario = print(f'{resto} ({contador})')
        contador *= 2
        numero_bin = divisor
        divisor //= 2
        resto %= 2
    print('-----------------------------------------------')
    print(f'{numero} na base hexadecimal: ')
    contador_hex = 1
    hexadecimal = ''
    while numero_hex != 0:
        divisorhex = numero_hex // 16
        restohex = numero_hex % 16
        nomenclatura = restohex
        if nomenclatura == 10:
            nomenclatura = 'A'
        elif nomenclatura == 11:
            nomenclatura = 'B'
        elif nomenclatura == 12:
            nomenclatura = 'C'
        elif nomenclatura == 13:
            nomenclatura = 'D'
        elif nomenclatura == 14:
            nomenclatura = 'E'
        elif nomenclatura == 15:
            nomenclatura = 'F'
        hexadecimal = f'{nomenclatura}{hexadecimal}'
        numero_hex = divisorhex
    print(hexadecimal)

main()