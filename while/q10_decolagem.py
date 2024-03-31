#Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave pode levantar vôo ou não. Considere os seguintes critérios:
#· O peso de decolagem da aeronave é sempre igual a 500.000 kg;
#· O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos passageiros; 
#· O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
#· A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
#· O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
#· O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua bagagem; cada passageiro tem o peso estimado de     70kg e cada volume de bagagem tem o peso estimado de 10kg.

#O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma mensagem indicando a liberação da decolagem ou não.

def main():
    
    combustivel = int(input('Combustivel, em litros, para a viagem: '))
    if combustivel < 10000:
        print('Quantidade de combustivel inadequada para vôo!!!     Mínimo necessário para decolagem: 10000 Litros')
    peso_do_combustivel = combustivel * 1.5

    numero_de_containers = int(input('Número de conteiners na viagem: '))
    peso_de_containers = 0
    while numero_de_containers != 0: #Dados dos Conteiners
        contador_conteiner = numero_de_containers
        peso_de_containers = int(input(f'Peso do {contador_conteiner}° conteiner na viagem: ')) + peso_de_containers
        numero_de_containers -= 1
        contador_conteiner -= 1
        peso_carga = peso_de_containers

    bilhete = 1
    bagagem = 0
    contador_passageiro = 0
    while bilhete != 0: #Dados dos Passageiros
        bilhete = int(input('Número do bilhete do passageiro: '))
        if bilhete == 0:
            break
        contador_passageiro += 1
    
        bagagem = int(input(f'Quantidade de bagagens do passageiro com o bilhete de número {bilhete}: ')) + bagagem
        peso_bagagem = bagagem


    peso_passageiro = 70 * contador_passageiro
    soma_das_cargas = peso_bagagem + peso_passageiro + peso_carga + peso_do_combustivel

    print('------------------------------')
    print(f'Quantidade de passageiros: {contador_passageiro}')
    print(f'Volume de bagagem: {peso_bagagem * 10}')
    print(f'Peso dos passageiros: {peso_passageiro}')
    print(f'Peso da carga: {peso_carga}')
    print(f'Peso do combustivel: {peso_do_combustivel}')
    print(f'Peso total: {soma_das_cargas}')
    print('------------------------------')

    peso_de_decolagem = 500000
    if peso_de_decolagem < soma_das_cargas:
        print('DECOLAGEM NÃO PERMITIDA')
    else:
        print('DECOLAGEM PERMITIDA')

main()