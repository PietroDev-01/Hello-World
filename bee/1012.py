def main():
    entradas = input().split(' ')
    A = float(entradas[0])
    B = float(entradas[1])
    C = float(entradas[2])
    
    Triangulo = (A * C) / 2
    Circulo = 3.14159 * C**2
    Trapezio = ((A + B) * C) / 2
    Quadrado = B**2
    Retangulo = A * B

    print(f'''TRIANGULO: {Triangulo:.3f}
CIRCULO: {Circulo:.3f}
TRAPEZIO: {Trapezio:.3f}
QUADRADO: {Quadrado:.3f}
RETANGULO: {Retangulo:.3f}''')
    
main()