

while  True:
    print()
    print('1 Fatorial')
    print('2 Quadrado')
    print('3 Cubo')
    print('4 Tabuada')
    print('0 Sair')
    menu = int(input('Escolha uma das opscoes'))
    if menu == 1:
        numero = int(input("Escolha um numero para a fatorial "))
        resultado=1
        fatorial=1
        while fatorial <= numero:
            resultado *= fatorial
            fatorial += 1
        print(resultado)
    elif menu == 2:
        num3 = int(input('Selecione um numero para fazer ao quadrado'))
        num4 = num3*num3
        print(num4)      
    elif menu == 3:
        num = int(input('selecione um numero'))
        num2 = num * num * num
        print('O cubo desse numero e', num2)
    elif menu == 4:
        num5 = int(input('Digite um numero'))
        print(num5, 'x 1 =', num5*1)
        print(num5, 'x 2 =', num5*2)
        print(num5, 'x 3 =', num5*3)
        print(num5, 'x 4 =', num5*4)
        print(num5, 'x 5 =', num5*5)
        print(num5, 'x 6 =', num5*6)
        print(num5, 'x 7 =', num5*7)
        print(num5, 'x 8 =', num5*8)
        print(num5, 'x 9 =', num5*9)
        print(num5, 'x 10 =', num5*10)
        
    elif menu == 0:
        print('A sessao foi encerrada')
        break
        

