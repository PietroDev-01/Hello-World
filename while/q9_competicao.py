def main():

    prova = 1
    clube_a = 0
    clube_b = 0

    while prova != 0:
        prova = int(input('Digite o numero da prova: '))

        if prova == 0:
            break
        else:
            nome = str(input('Digite o nome do competidor: '))
            tempo = int(input(f'Digite o tempo do competidor {nome}, em segundos na prova {prova}: '))
            classificacao = int(input(f'Digite a classificação do competidor {nome} na prova {prova}: '))
            clube_competidor = str(input(f'Digite o clube do competidor {nome}(clube A ou clube B): '))

            if clube_competidor == 'a'  or clube_competidor == 'A':
                clube_a += pontuação(classificacao)
            elif clube_competidor == 'b' or clube_competidor == 'B':
                clube_b += pontuação(classificacao)
            else:
                print(f'o clube "{clube_competidor}" é INVÁLIDO')
                break
    if clube_a > clube_b:
        print(f'O clube A é vencedor com {clube_a} pontos, visto que o clube B efetuou apenas {clube_b} pontos')
    elif clube_b > clube_a:
        print(f'O clube B é vencedor com {clube_b} pontos, visto que o clube B efetuou apenas {clube_a} pontos')
    else:
        print(f'O jogo EMPATOU visto a mesma quantidade de pontos entre os dois clubes!!! {clube_a} pontos para o clube A e {clube_b} pontos para o clube B.')

def pontuação(classificacao):

    if classificacao == 1:
        return 9
    elif classificacao == 2:
        return 6
    elif classificacao == 3:
        return 4
    elif classificacao == 4:
        return 3
    else:
        return 0
    
main()