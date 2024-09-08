def main():
    valor_de_entrada = float(input())
    qtd_de_notas100 = valor_de_entrada // 100 
    resto_de_100 = valor_de_entrada % 100
    qtd_de_notas50 = resto_de_100 // 50
    resto_de_50 = resto_de_100 % 50
    qtd_de_notas20 = resto_de_50 // 20
    resto_de_20 = resto_de_50 % 20
    qtd_de_notas10 = resto_de_20 // 10
    resto_de_10 = resto_de_20 % 10
    qtd_de_notas5 = resto_de_10 // 5
    resto_de_5 = resto_de_10 % 5
    qtd_de_notas2 = resto_de_5 // 2
    resto_de_2 = resto_de_5 % 2
    qtd_de_notas1 = resto_de_2 // 1
    resto_de_1 = resto_de_2 % 1

    qtd_de_moedas50 = resto_de_1 // 0.50
    resto_de_M50 = resto_de_1 % 0.50
    qtd_de_moedas25 = resto_de_M50 // 0.25
    resto_de_M25 = resto_de_M50 % 0.25
    qtd_de_moedas10 = resto_de_M25 // 0.10
    resto_de_M10 = resto_de_M25 % 0.10
    qtd_de_moedas5 = resto_de_M10 // 0.05
    resto_de_M5 = resto_de_M10 % 0.05
    qtd_de_moedas1 = resto_de_M5 / 0.01

    print(f'''NOTAS:
{qtd_de_notas100:.0f} nota(s) de R$ 100.00
{qtd_de_notas50:.0f} nota(s) de R$ 50.00
{qtd_de_notas20:.0f} nota(s) de R$ 20.00
{qtd_de_notas10:.0f} nota(s) de R$ 10.00
{qtd_de_notas5:.0f} nota(s) de R$ 5.00
{qtd_de_notas2:.0f} nota(s) de R$ 2.00
MOEDAS:
{qtd_de_notas1:.0f} moeda(s) de R$ 1.00
{qtd_de_moedas50:.0f} moeda(s) de R$ 0.50
{qtd_de_moedas25:.0f} moeda(s) de R$ 0.25
{qtd_de_moedas10:.0f} moeda(s) de R$ 0.10
{qtd_de_moedas5:.0f} moeda(s) de R$ 0.05
{qtd_de_moedas1:.0f} moeda(s) de R$ 0.01''')

main()