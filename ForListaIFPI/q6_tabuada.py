#6. Escreva a tabuada dos números de 1 a 10.

def main():
    print('Tabuada de 1 a 10')

    multiplosde1 = [0,1,2,3,4,5,6,7,8,9,10]
    multiplosde2 = [0,2,4,6,8,10,12,14,16,18,20]
    multiplosde3 = [0,3,6,9,12,15,18,21,24,27,30]
    multiplosde4 = [0,4,8,12,16,20,24,28,32,36,40]
    multiplosde5 = [0,5,10,15,20,25,30,35,40,45,50]
    multiplosde6 = [0,6,12,18,24,30,36,42,48,54,60]
    multiplosde7 = [0,7,14,21,28,35,42,49,56,63,70]
    multiplosde8 = [0,8,16,24,32,40,48,56,64,72,80]
    multiplosde9 = [0,9,18,27,36,45,54,63,72,81,90]
    multiplosde10 = [0,10,20,30,40,50,60,70,80,90,100]

    multiplicador1 = 0
    multiplicador2 = 0
    multiplicador3 = 0
    multiplicador4 = 0
    multiplicador5 = 0
    multiplicador6 = 0
    multiplicador7 = 0
    multiplicador8 = 0
    multiplicador9 = 0
    multiplicador10 = 0
    print('TABUADA DE 1')
    for tabuada1 in multiplosde1:
        numero = 1
        print(f'{numero} x {multiplicador1} = {tabuada1}')
        multiplicador1 += 1
    print('')

    print('TABUADA DE 2')
    for tabuada2 in multiplosde2:
        numero = 2
        print(f'{numero} x {multiplicador2} = {tabuada2}')
        multiplicador2 += 1
    print('')

    print('TABUADA DE 3')
    for tabuada3 in multiplosde3:
        numero = 3
        print(f'{numero} x {multiplicador3} = {tabuada3}')
        multiplicador3 += 1
    print('')

    print('TABUADA DE 4')
    for tabuada4 in multiplosde4:
        numero = 4
        print(f'{numero} x {multiplicador4} = {tabuada4}')
        multiplicador4 += 1
    print('')

    print('TABUADA DE 5')
    for tabuada5 in multiplosde5:
        numero = 5
        print(f'{numero} x {multiplicador5} = {tabuada5}')
        multiplicador5 += 1
    print('')
    
    print('TABUADA DE 6')
    for tabuada6 in multiplosde6:
        numero = 6
        print(f'{numero} x {multiplicador6} = {tabuada6}')
        multiplicador6 += 1
    print('')

    print('TABUADA DE 7')
    for tabuada7 in multiplosde7:
        numero = 7
        print(f'{numero} x {multiplicador7} = {tabuada7}')
        multiplicador7 += 1
    print('')

    print('TABUADA DE 8')
    for tabuada8 in multiplosde8:
        numero = 8
        print(f'{numero} x {multiplicador8} = {tabuada8}')
        multiplicador8 += 1
    print('')

    print('TABUADA DE 9')
    for tabuada9 in multiplosde9:
        numero = 9
        print(f'{numero} x {multiplicador9} = {tabuada9}')
        multiplicador9 += 1
    print('')

    print('TABUADA DE 10')
    for tabuada10 in multiplosde10:
        numero = 10
        print(f'{numero} x {multiplicador10} = {tabuada10}')
        multiplicador10 += 1
    print('')
main()