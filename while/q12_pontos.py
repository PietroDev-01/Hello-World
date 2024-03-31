#Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e  responda quem ganha a partida. A partida chega ao final se: · Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2. · Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma diferença de 2 pontos sobre o adversário.

def main():
    ponto_jogador1 = 0
    ponto_jogador2 = 0
    contador = 1
    while ponto_jogador1 < 21 and ponto_jogador2 < 21 and ponto_jogador1 - ponto_jogador2 <= 21:
        if ponto_jogador2 > 21 and ponto_jogador2 - ponto_jogador1 <= 2:
            break
        else:
            ponto_jogador1 = int(input(f' ({contador}° Rodada) 1° Jogador Pontos acumulados: {ponto_jogador1} --- pontos adicionais: ')) + ponto_jogador1
            ponto_jogador2 = int(input(f' ({contador}° Rodada)  2° Jogador Pontos acumulados: {ponto_jogador2} --- pontos adicionais: ')) + ponto_jogador2

            contador += 1
            if ponto_jogador2 == ponto_jogador1:
                while ponto_jogador1 >= 21 and ponto_jogador2 >= 21 and ponto_jogador1 - ponto_jogador2 <= 1:
                                ponto_jogador1 = int(input(f' ({contador}° Rodada)  1° Jogador Pontos acumulados: {ponto_jogador1} --- pontos adicionais: ')) + ponto_jogador1
                                ponto_jogador2 = int(input(f' ({contador}° Rodada)  2° Jogador Pontos acumulados: {ponto_jogador2} --- pontos adicionais: ')) + ponto_jogador2

                                contador += 1

    if ponto_jogador1 > ponto_jogador2:
        print('Jogador 1 venceu')
        print(f'Pontos acumulados jogador 1: {ponto_jogador1}')
        print(f'Pontos acumulados jogador 2: {ponto_jogador2}')
    elif ponto_jogador2 > ponto_jogador1:
        print('Jogador 2 venceu')
        print(f'Pontos acumulados jogador 1: {ponto_jogador1}')
        print(f'Pontos acumulados jogador 2: {ponto_jogador2}')

main()