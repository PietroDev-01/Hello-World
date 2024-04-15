#20. Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de 600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
#· Distância percorrida desde a última medição;
#· Quantidade de litros consumidos para percorrer a distância indicada.
#       Escreva um algoritmo que leia estas informações e escreva:
#· se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
#· se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
#· o consumo em km/l do carro.

def main():
    distancia = int(input('Distância a ser percorrida: '))
    tanque = int(input('Capacidade Máxima do tanque no Veículo: '))
    print(f'distância do trajeto: {distancia}; Capacidade do tanque de gasolina: {tanque}')
    medidor = input('Acionar medidor?(S ou N): ').upper()
    if medidor == 'N':
        print('     Sem o medidor acionado uma análise individual de desempenho do veículo é invíavel')
    else:
        distancia_percorrida_acumulo = 0
        Consumo_gasolina_acumulo = 0
        while medidor == 'S':
            distancia_percorrida = int(input('Distância percorrida até o momento: '))
            Consumo_gasolina = int(input('Consumo de gasolina até o momento: '))
            distancia_percorrida_acumulo += distancia_percorrida
            Consumo_gasolina_acumulo += Consumo_gasolina
            Consumo_viajem = distancia_percorrida_acumulo / Consumo_gasolina_acumulo

            if distancia_percorrida_acumulo >= distancia:
                print('')
                print(f'        O Veículo chegou ao destino com {distancia_percorrida_acumulo}Km percorridos!!!')
                print(f'        O Veículo chegou ao Destino com o consumo de combustivel igual a: {Consumo_viajem:.1f}Km/L')
                break
            if Consumo_gasolina_acumulo >= tanque:
                print('')
                print('    O Veículo não chegou ao destino devido à falta de combustível!!!')
                print(f'                   Distância percorrida até "Prego": {distancia_percorrida_acumulo}Km')
                print(f'    Consumo de combustivel Total: {Consumo_gasolina_acumulo}    |    Consumo combustivel, em Km/L: {Consumo_viajem:.1f} Km/L')
                break
            print('-----------------------------------------')
            medidor = input('Acionar Medidor Novamente?(S ou N): ').upper()
    
main()