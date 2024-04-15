#Uma companhia financeira debita um juro de 0.85% diário sobre o saldo não pago de um empréstimo. Com um empréstimo de R$ 3.000,00, um pagamento de R$ 200,00 é feito todo dia útil. Escreva um  algoritmo que calcule quantos dias úteis são necessários para se concluir o pagamento do empréstimo.

def main():
    juros_diario = float(input('Ponha a taxa de juros diário(Em %): ')) / 100 
    emprestimo = int(input('Valor do Emprestimo requerido: '))
    emprestimo_inicial = emprestimo
    pagamento = int(input('Valor do pagamento diário para quitação da divida: '))
    contador = 0
    saida = ''
    while emprestimo > 0:
        aumento_diario = emprestimo * juros_diario
        emprestimo_com_aumento = emprestimo + aumento_diario
        contador += 1
        if pagamento > emprestimo:
            saida = print(f'Valor após {contador}° pagamento: R$0.00')
            break
        emprestimo = emprestimo_com_aumento - pagamento
        saida = print(f'Valor após {contador}° pagamento: R${emprestimo:.2f}')
    
    print(saida)
    print(f'São necessários {contador} dias úteis pagando R${pagamento:.2f} para quitar o empréstimo de {emprestimo_inicial}')

main()