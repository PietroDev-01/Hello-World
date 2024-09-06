def main():
    entrada1 = input().split(' ')
    entrada2 = input().split(' ')
    codigo1 = entrada1[0]; codigo2 = entrada2[0]
    numero_pecas1 = entrada1[1]; numero_pecas2 = entrada2[1]
    valor_unitario = entrada1[2]; valor_unitario2 = entrada2[2]

    valor_final = (int(numero_pecas1) * float(valor_unitario)) + (int(numero_pecas2) * float(valor_unitario2))

    print(f'VALOR A PAGAR: R$ {valor_final:.2f}')

main()