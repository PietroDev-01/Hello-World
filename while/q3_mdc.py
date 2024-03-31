#Leia 2 (dois) números, calcule e escreva o mdc (máximo divisor comum) entre os números lidos.
def calcular_mdc(a, b):
    maior = max(a, b)
    menor = min(a, b)

    mdc = menor

    while maior % mdc != 0 or menor % mdc != 0:
        mdc -= 1

    return mdc

def main(): 
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    mdc = calcular_mdc(num1, num2)

    print(f"O MDC de {num1} e {num2} é: {mdc}")

main()