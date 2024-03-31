def calcular_salario(salario):
    if salario < 3000 and salario > 0:
        return (salario * 0.25)+ salario
    elif salario < 6000:
        return salario * 0.2 + salario
    elif salario < 10000:
        return salario * 0.15 + salario
    else:
        return salario * 0.1 + salario


def main():
    contador_salario = 1
    salario = 1
    salarios_atuais = 0
    salarios_reajustado = 0 

    while salario != 0:
        salario = int(input(f'Digite o {contador_salario}° salario: R$'))
        salarios_atuais += salario
        contador_salario += 1

        if salario == 0 :
            break
        else:
            numero = calcular_salario(salario)
            salarios_reajustado += numero
            reajuste_unt = numero
            print(f'Salário n°{contador_salario - 1} com reajuste: R${reajuste_unt:.2f}')
    
    diferença = salarios_reajustado - salarios_atuais 
    print('---------------------------------------')
    print(f'Soma dos salários atuais: R${salarios_atuais:.2f}')
    print(f'Soma dos salários reajustados: R${salarios_reajustado:.2f}')
    print(f'Diferença entre salários R${diferença:.2f}')

main()