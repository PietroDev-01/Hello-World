#7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido

def main():
    print('!!! Some números entre 1 e N !!!')
    limite = int(input('O Número limite da soma: '))
    print('')
    
    contador = 0
    add = 0
    for soma in range(1 + 1, limite):
        soma = soma + contador
        contador = soma
        add +=1 
        print(f' {add}° soma = {soma}')


    print('')
main()