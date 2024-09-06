import math
def main ():
    entrada_1 = input().split(' ')
    entrada_2 = input().split(' ')

    valor_de_x1 = float(entrada_1[0]); valor_de_y1 = float(entrada_1[1])
    valor_de_x2 = float(entrada_2[0]); valor_de_y2 = float(entrada_2[1])

    distancia = math.sqrt((valor_de_x2 - valor_de_x1)**2 + (valor_de_y2 - valor_de_y1)**2)

    print(f'{distancia:.4f}')
main()