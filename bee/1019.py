def main():
    segundos_totais = int(input())
    segundos = segundos_totais % 60
    if segundos_totais < 3600:
        minutos = segundos_totais // 60
    else:
        minutos = (segundos_totais % 3600) // 60
    horas = segundos_totais // 3600
    print(f'{horas}:{minutos}:{segundos}')
main()