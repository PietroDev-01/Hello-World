def main():
  numero = 1

  while numero != 0:
        numero = int(input('Número: '))
        mostrar_divisores(numero)
    
  print('Fim..')

def mostrar_divisores(numero):
    print(f'Divisores de {numero}: ')

    candidato = numero
    contador = 0
    divisores = ''
  
    while candidato > 0:
        if eh_divisor(numero, candidato):
            contador += 1
            divisores = print(f'{candidato}')
        
        candidato -= 1
    print(divisores)
    print(f'Total de Divisores: {contador}')


def eh_divisor(numero, candidato):
  return numero % candidato == 0

main()