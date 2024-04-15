#17. Em um concurso de beleza, cada candidata tem um cartão contendo nome, altura e peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o nome e a altura da candidata mais alta e da mais baixa; o nome e o peso da candidata mais magra e da mais gorda. (Flag: nome = 'FIM').

def main():
    mais_magra = float('inf')
    mais_baixa = float('inf')
    mais_gorda = float('-inf')
    mais_alta = float('-inf')

    nome = ''
    nome_mais_alta = ''
    nome_mais_baixa = ''
    nome_mais_gorda = ''
    nome_mais_magra = ''
    while nome != 'FIM':
        nome = input('qual seu nome?: ').upper()
        if nome == 'FIM':
            break
        altura = float(input('qual sua altura?: '))
        peso = float(input('qual o seu peso?: '))
        if altura > mais_alta:
            mais_alta = altura
            nome_mais_alta = nome
        elif altura < mais_baixa:
            mais_baixa = altura
            nome_mais_baixa = nome
        
        if peso > mais_gorda:
            mais_gorda = peso
            nome_mais_gorda = nome
        elif peso < mais_magra:
            mais_magra = peso
            nome_mais_magra = nome

    print(f'A candidata mais alta é {nome_mais_alta} com {mais_alta:.2f}m')
    print(f'A candidata mais baixa é {nome_mais_baixa} com {mais_baixa:.2f}m')
    print(f'A candidata mais magra é {nome_mais_magra} com {mais_magra:.1f}kg')
    print(f'A candidata mais gorda é {nome_mais_gorda} com {mais_gorda:.1f}kg')


main()
