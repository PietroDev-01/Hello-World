def calcular_media(x,y,z):
    return (x*2)+(y*3)+(z*5)/ 10

def main():

    matricular = 1
    aprovados = 0
    reprovados = 0
    total_alunos = 0
    while matricular != 0:
        matricular = int(input('Digite a matricular do aluno: '))

        if matricular == 0:
            break
        else:
            total_alunos += 1
            nota_1 = int(input('Nota 1: '))
            nota_2 = int(input('Nota 2: '))
            nota_3 = int(input('Nota 3: '))

            if calcular_media(nota_1,nota_2,nota_3) >= 7:
                print(f'Aprovado')
                aprovados += 1
            else:
                print(f'Reprovado')
                reprovados += 1
    print(f'total de aprovados:{aprovados} total de reprovados:{reprovados} total de alunos:{total_alunos}')

main()