tri = int(input('Selecione a medida de um lado'))
tri2 = int(input('Seleciione a medida de outro lado'))
tri3 = int(input('Seleciione a medida do outro lado'))

if tri == tri2 and tri == tri3 and tri3 == tri2:
    print('O triangulo e equilatero')
elif tri == tri2 or tri2 == tri3 or tri == tri3:
    print('O triangulo é isosceles')
elif tri != tri2 and tri != tri2 and tri3 != tri2:
    print('O triangulo é escaleno')
    
