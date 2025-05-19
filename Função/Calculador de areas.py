
def area_retangulo(lado1, lado2):
    resultado = lado1 * lado2
    return resultado

def area_quadrado(lado3, lado4):
    resultado1 = lado3 * lado4
    return resultado1

def area_circulo(lado5):
    pi = 3.14
    resultado2= pi * (lado5**2)
    return  resultado2
def area_triangulo(lado6):
    resultado3 = lado6 * lado6
    raiz = round(3 ** 0.5)
    multi = resultado3 * raiz
    area = multi / 4
    return area
def area_hexagono(lado7):
    l2 = lado7 * lado7
    raiz = round(3 ** 0.5)
    l4 = l2 * raiz
    at = l4 / 4
    hexagono = 6 * at
    return hexagono
    
def menu_perimetro():
    print('')
    print('1 - perimetro do circulo')
    print('2 - perimetro do retangulo')
    print('3 - perimetro do quadrado')
    print('4 - perimetro do triangulo')
    print('5 - perimetro do hexagono')
    perimetro = int(input('Escolha uma das opcoes'))
    if perimetro == 1:
        formula = int(input('Escolha a raiz do circulo'))
        print((2 * 3.14) * formula)
    elif perimetro == 2:
        formula2 = int(input('Escolha o primeiro lado do retangulo'))
        formula3 = int(input('Escolha o segundo lado do retangulo'))
        print(formula2 + formula3 + formula2 + formula3)
    elif perimetro == 3:
        formula4 = int(input('Escolha o lado do quadrado'))
        print(formula4 * 4)
    elif perimetro == 4:
        formula5 = int(input('Escolha o primeiro lado do retangulo'))
        formula6 = int(input('Escolha o segundo lado do retangulo'))
        formula7 = int(input('Escolha o terceiro lado do retangulo'))
        print(formula5 + formula6 + formula7)
    elif perimetro == 5:
        formula8 = int(input('Escolha o lado do hexagono'))
        print(formula8 * 6)
        
def menu_areas():
    print('1 - Area do circulo')
    print('2 - Area do retangulo')
    print('3 - Area do quadrado')
    print('4 - Area do triangulo')
    print('5 - Area do hexagono')

    menu = int(input('Escolha uma das opcoes'))
    if menu == 1:
        lado5 = int(input('Escolha o raio do circulo'))
        print(area_circulo(lado5))
    elif menu == 2:
        lado1 = int(input('Escolha a altura'))
        lado2 = int(input('Escolha a base'))
        print(area_retangulo(lado1, lado2))
    elif menu == 3:
        lado3 = int(input('Escolha o lado'))
        lado4 = int(input('Escolha o outro lado'))
        print(area_quadrado(lado3, lado4))
    elif menu == 4:
        lado6 = int(input('Escolha o lado do triangulo'))
        print(area_triangulo(lado6))
    elif menu == 5:
        lado7 = int(input('Escolha o lado do triangulo'))
        print(area_hexagono(lado7))
    else:
        print('Escolha um numero valido')
    
    
    
print('1 - Calcular a area')
print('2 - Calcular o perimetro')

num1 = int(input('Escolha um dos numeros'))        
if  num1 == 2:
    menu_perimetro()
elif num1 == 1:
    menu_areas()
    
    
   







