#2. Leia N e escreva todos os números inteiros pares de 1 a N.
def main():
    print('           !!! Veja quais são os números pares entre 1 e um número escolhido por você !!!')
    numero = int(input('Número de sua escolha aqui: '))
    print(f'                          Lista de números pares entre 1 e {numero}: ')
    contadorN = 0
    for lista in range (2, numero, 2):
        contadorN += 1   
        print(f'{contadorN}° Número par - {lista}')
main()