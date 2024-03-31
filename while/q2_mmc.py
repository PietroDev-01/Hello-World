#Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.

def main():

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    mmc = calcular_mmc(num1, num2)

    print(f"O MMC de {num1} e {num2} é: {mmc}")

def calcular_mmc(a, b):

    maior = max(a, b)
    menor = min(a, b)

    mmc = maior

    while mmc % menor != 0:
        mmc += maior

    return mmc

main()