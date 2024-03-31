# Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo 
# quando a soma de dois números consecutivos da lista for igual a X.

def main():
    numero_x = int(input('Número x: '))

    soma_numeros_lista = 0
    contador_lista1 = 1
    contador_lista2 = 1
    while soma_numeros_lista != numero_x:
        lista1 = int(input(f' {contador_lista1}° Numero na lista um: '))
        contador_lista1 +=1
        lista2 = int(input(f' {contador_lista2}° Numero na lista dois: '))
        contador_lista2 += 1
        soma_numeros_lista = lista1 + lista2

    print(f'A soma do {contador_lista1 - 1}° número da lista um "{lista1}" com o {contador_lista2 - 1}° número da lista dois "{lista2}" é igual ao número x: "{numero_x}"')
main()