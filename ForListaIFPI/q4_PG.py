#4. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.

def main():
    print('                                         !!! Crie sua própria Progressão Geométrica !!!')
    print('')
    numeroinicial = int(input('Insira o Número inical da Progressão Geométrica: '))
    razaoPG = int(input('Escreva a Razão da sua Progressão Geométrica: '))
    limitePG = int(input('Insira o limite da sua Progressão Geométrica: '))
    print('')
    contadorNumeros = 0

    if razaoPG == 0:
        print(f'Essa PG é infinita e possui todos os termos iguais a "0", Decorrente da sua Razão = 0')
    elif razaoPG == 1:
        print(f'Essa PG é infinita e possui todos os termos iguais a "{numeroinicial}", Decorrente da sua Razão = 1')
    elif razaoPG == -1:
        print(f'Essa PG é infinita e possui todos os termos iguais a "{numeroinicial}" e "{-numeroinicial}", Decorrente da sua Razão = -1')
    elif numeroinicial == limitePG:
        print('Considere não igualar o valor inicial ao valor limite para assim fazer uma PG real')
    elif numeroinicial > 0 and razaoPG > 0 and limitePG < numeroinicial:
        print('PG incalculável, tendo em vista o limite menor que o número inicial e uma razão positiva')
    elif numeroinicial < 0 and razaoPG < 0 and limitePG > numeroinicial:
        print('PG incalculável, tendo em vista o limite maior que o número inicial e uma razão negativa')
    else:
        
        if numeroinicial > 0 and limitePG > numeroinicial and razaoPG > 0: #PG Crescente
                
            colecaoPG = []
            while numeroinicial < limitePG:
                colecaoPG.append(numeroinicial)
                numeroinicial = numeroinicial * razaoPG
                if numeroinicial >= limitePG:
                    break
                

            for PG in colecaoPG:
                contadorNumeros += 1
                print(f'                Termo A{contadorNumeros} da PG: {PG}')

            print('')
            print('     PG do tipo: CRESCENTE')

        elif numeroinicial > 0 and razaoPG < 0 or numeroinicial < 0 and limitePG < numeroinicial and razaoPG < 0: #PG Oscilante

            colecaoPG = []
            while limitePG > numeroinicial:
                colecaoPG.append(numeroinicial)
                numeroinicial = numeroinicial * razaoPG
                if limitePG <= numeroinicial or numeroinicial <= -limitePG :
                    break
            
            while limitePG < numeroinicial:
                colecaoPG.append(numeroinicial)
                numeroinicial = numeroinicial * razaoPG
                if limitePG >= numeroinicial or numeroinicial >= -limitePG :
                    break

            for PG in colecaoPG:
                contadorNumeros += 1
                print(f'                Termo A{contadorNumeros} da PG: {PG}')
                
            print('')
            print('     PG do tipo: OSCILANTE')
        
        elif numeroinicial < 0 and limitePG < numeroinicial: #PG decrescente

            colecaoPG = []
            while limitePG < numeroinicial:
                colecaoPG.append(numeroinicial)
                numeroinicial = numeroinicial * razaoPG
                if limitePG >= numeroinicial:
                    break
            
            for PG in colecaoPG:
                contadorNumeros += 1
                print(f'                Termo A{contadorNumeros} da PG: {PG}')
                
            print('')
            print('     PG do tipo: DECRESCENTE')


    print('')
main()