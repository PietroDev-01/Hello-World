def main():
    valor_de_entrada = int(input(''))
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

    print(f'''{valor_de_entrada}
{qtd_de_notas100} nota(s) de R$ 100,00
{qtd_de_notas50} nota(s) de R$ 50,00
{qtd_de_notas20} nota(s) de R$ 20,00
{qtd_de_notas10} nota(s) de R$ 10,00
{qtd_de_notas5} nota(s) de R$ 5,00
{qtd_de_notas2} nota(s) de R$ 2,00
{qtd_de_notas1} nota(s) de R$ 1,00''')
    
main()