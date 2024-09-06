def main():
    distancia_percorrida = int(input())
    combustivel_gasto = float(input())

    consumo_medio = distancia_percorrida / combustivel_gasto

    print(f'{consumo_medio:.3f} km/l')
main()
