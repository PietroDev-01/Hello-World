def main():
    entradas = input().split(' ')
    valor_1 = int(entradas[0]); valor_2 = int(entradas[1]); valor_3 = int(entradas[2])
    Maior_entre_A_e_B = (valor_1 + valor_2 + abs (valor_1 - valor_2)) / 2
    if Maior_entre_A_e_B < valor_3:
        Maior_entre_A_e_B = valor_3
        print(f'{Maior_entre_A_e_B:.0f} eh o maior')
    else:
        print(f'{Maior_entre_A_e_B:.0f} eh o maior')
main()