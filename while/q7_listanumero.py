#Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.

def main():
    numero_lido = int(input('Número desejado: '))
    
    contador = 1
    lista_numero = 0
    while numero_lido != lista_numero:
        lista_numero = int(input(f'{contador}° - lista de números: '))
        if numero_lido != lista_numero:
            contador += 1
            continue
        else:
            break
    print(f'O número desejado {numero_lido} é igual ao número da lista {lista_numero} que encontra-se na {contador}° posição')
main()
