# Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O 
# entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então 
# responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada 
# entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
# · a porcentagem de cada candidato;
# · a porcentagem dos outros candidatos;
# · a porcentagem de eleitores indecisos;
# · a porcentagem de votos nulos/brancos;
# · o total de entrevistados;
# · uma mensagem indicando a possibilidade ou não de haver 2º turno

def main():
    print('---------------------------------------------------------------------------------------------------------------------------------')
    print('INSTRUÇÕES DE VOTO: VOTE 45 PARA SERRA ... VOTE 13 PARA DILMA ... VOTE 23 PARA CIRO GOMES ... VOTE 99 SE INDECISO ... VOTE 98 PARA OUTROS ... VOTE 0 PARA BRANCO/NULO    ')
    print('---------------------------------------------------------------------------------------------------------------------------------')
    
    total_votos = 0
    serra = 0
    dilma = 0
    ciro_gomes = 0
    indeciso = 0
    outros = 0
    nulo = 0
    opiniao = 1
    while opiniao != -1:
        opiniao = int(input(f'(Eleitor n°{total_votos + 1}) Disque seu número para voto: '))

        if opiniao == 45:
            serra = serra + 1
            total_votos += 1
        elif opiniao == 13:
            dilma = dilma + 1
            total_votos += 1
        elif opiniao == 23:
            ciro_gomes += 1
            total_votos += 1
        elif opiniao == 99:
            indeciso += 1
            total_votos += 1
        elif opiniao == 98:
            outros += 1
            total_votos += 1
        elif opiniao == 0:
            nulo += 1
            total_votos += 1
    
    print('-------------------------------------')
    print(f'Total de entrevistados: {total_votos}')
    print(f'Total de Eleitores em Serra: {serra}')
    print(f'Total de Eleitores em Dilma: {dilma}')
    print(f'Total de Eleitores em Ciro Gomes: {ciro_gomes}')
    print(f'Total de Eleitores Indecisos: {indeciso}')
    print(f'Total de Votos em outros: {outros}')
    print(f'Total de Votos nulos: {nulo}')
        
main()