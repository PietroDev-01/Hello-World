#18. Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,  crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão necessários, para que a população da cidade A ultrapasse a população da cidade B.

def main():
    print('                     Descubra quando a população de uma Cidade ultrapassará a outra!!!                       ')
    CidadeA = input('Nome da Cidade que ultrapassará, em quesito populacional, a cidade seguinte: ')
    CidadeB = input('Nome da Cidade que será ultrapassada: ')
    PopulacaoCidadeA = int(input(f'População de {CidadeA}: '))
    PopulacaoinicialA = PopulacaoCidadeA
    PopulacaoCidadeB = int(input(f'População de {CidadeB}: '))
    if PopulacaoCidadeA > PopulacaoCidadeB:
        print(f'A população de {CidadeA} já é maior que a população de {CidadeB}!!!')
    else:
        PopulacaoinicialB = PopulacaoCidadeB
        TaxaDeCrescimentoA = float(input(f'Taxa de Crescimento Populacional Anual de {CidadeA}: ')) / 100
        TaxaDeCrescimentoB = float(input(f'Taxa de Crescimento Populacional Anual de {CidadeB}: ')) / 100
        AnoInicial = int(input('Ano inicial para comparação: '))
        Comparacao = ''
        ContadorAnos = 0

        while PopulacaoCidadeA < PopulacaoCidadeB:
            if PopulacaoinicialA > PopulacaoinicialB:
                print(f'A população de {CidadeA} já é maior que a poplução de {CidadeB}!!!')
                break
            elif TaxaDeCrescimentoA <= TaxaDeCrescimentoB:
                print(f'A População de {CidadeA} nunca ultrapassará a População de {CidadeB}, por conta da Taxa de Crescimento!!!')
                break
            else:
                AnoInicial += 1
                ContadorAnos += 1
                CalculoA = PopulacaoCidadeA * TaxaDeCrescimentoA
                CalculoA = round(CalculoA, 0)
                CalculoB = PopulacaoCidadeB * TaxaDeCrescimentoB
                CalculoB = round(CalculoB, 0)
                PopulacaoCidadeA += CalculoA
                PopulacaoCidadeB += CalculoB
                Comparacao = print(f'Ano: {AnoInicial}     Populaçao de {CidadeA}: {PopulacaoCidadeA}        População de {CidadeB}: {PopulacaoCidadeB}')

        if TaxaDeCrescimentoA <= TaxaDeCrescimentoB:
            print('                                 FIM                                         ')
        else:
            print(f'{Comparacao}')
            print(f'Apenas em {AnoInicial} que a População de {CidadeA} ultrapassará a Populaçao de {CidadeB}!!!')
            print(f'Exatamente {ContadorAnos} Ano(s) após o início da comparação')


main()