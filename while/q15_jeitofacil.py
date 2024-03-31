def main():
    print('Conversor de: decimal para: binário e hexadecimal')
    numero = int(input('Número de base decimal entre 0 e 255: '))
    if numero < 0 or numero > 255:
        print('Apenas números entre 0 e 255 são aceitos')
        return
    print(f'{numero} na base binária: ')
    print(bin(numero))
    print('-----------------------------------------------')
    print(f'{numero} na base hexadecimal: ')
    print(hex(numero))

main()
