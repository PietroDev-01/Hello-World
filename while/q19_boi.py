#19. Em um frigorífico, cada boi traz em seu pescoço um cartão contendo o seu n.º de identificação e seu  peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o n.º de identificação e o peso do  boi mais magro e do boi mais gordo. (Flag: n.º identificação=0)

def main():
    identificacao = 1
    identificacao_numeracao_gordo = []
    identificacao_numeracao_magro = []
    contador_peso_boi_gordo = []
    contador_peso_boi_magro = []
    contador_de_bois = 0

    while identificacao != 0:
        identificacao = int(input('Número de identificação do boi: '))
        if identificacao == 0:
            break
        else:
            contador_de_bois += 1
            identificacao_numeracao_gordo.append(identificacao)
            identificacao_numeracao_magro.append(identificacao)
            peso_do_boi = int(input('Peso do boi em Kg: '))
            contador_peso_boi_gordo.append(peso_do_boi)
            contador_peso_boi_magro.append(peso_do_boi)
            print('')

            if contador_peso_boi_gordo[0] > peso_do_boi:
                contador_peso_boi_gordo = contador_peso_boi_gordo
                identificacao_numeracao_gordo = identificacao_numeracao_gordo
            elif contador_peso_boi_gordo[0] < peso_do_boi:
                contador_peso_boi_gordo[0] = peso_do_boi
                identificacao_numeracao_gordo[0] = identificacao

            if contador_peso_boi_magro[0] < peso_do_boi:
                contador_peso_boi_magro = contador_peso_boi_magro
                identificacao_numeracao_magro = identificacao_numeracao_magro
            elif contador_peso_boi_magro[0] > peso_do_boi:
                contador_peso_boi_magro[0] = peso_do_boi
                identificacao_numeracao_magro[0] = identificacao

    
    if identificacao == 0:
        print('')
        print(f'        O boi mais gordo tem {contador_peso_boi_gordo[0]}Kg')
        print(f'        E o seu Número de identificação é: {identificacao_numeracao_gordo[0]}')
        print('')
        print(f'        O boi mais magro tem {contador_peso_boi_magro[0]}Kg')
        print(f'        E o seu Número de identificação é: {identificacao_numeracao_magro[0]}')
        print(f'                                                        Total de bois analisados: {contador_de_bois}')

main()