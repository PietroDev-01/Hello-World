#4. Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o resultado da última divisão efetuada.

def main():
    num = int(input('Digite um número: '))

    resultado = num
    print(f'1 - {num} / 2 é {num // 2}')
    contador = 2
    while num // 2 != 0:
        if resultado != 0:
            resultado = resultado // 2
            divisao = resultado // 2
            print(f'{contador} - {resultado} / 2 é {divisao}')
            contador += 1
        else:
         break

main()