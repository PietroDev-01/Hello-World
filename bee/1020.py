def main():
    idade_inicial_em_dias = int(input())

    idade_em_anos = idade_inicial_em_dias // 365 # 1 ano
    resto_de_idade_em_anos = idade_inicial_em_dias % 365 # 35 dias
    idade_em_mes = resto_de_idade_em_anos // 30 
    idade_em_dias = resto_de_idade_em_anos % 30 

    print(f'''{idade_em_anos} ano(s)
{idade_em_mes} mes(es)
{idade_em_dias} dia(s)''')

main()