 #Escreva um algoritmo para determinar o número de dígitos de um número informado.

def main():
    numero = int(input('Número experimental: '))
    numero_analise = numero

    resultado_divisao = numero_analise // 10
    digito = 1
    while numero_analise != 0:
        resultado_divisao = numero_analise // 10
        if resultado_divisao != 0:
            numero_analise = resultado_divisao
            digito += 1
        else:
            break
    
    print(f'O Número {numero} possui {digito} digito(s)')

main()