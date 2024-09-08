def main():
    tempo_de_viagem = int(input())
    velocidade_media = int(input())
    CONSUMO_AUTOMOVEL = 12

    qtd_de_litros_necessario = (velocidade_media * tempo_de_viagem) / CONSUMO_AUTOMOVEL

    print(f'{qtd_de_litros_necessario:.3f}')
main()