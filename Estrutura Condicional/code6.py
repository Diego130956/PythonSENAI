num1 = input('Selecione um numero')
num2 = input('Selecione um numero')
num3 = input('Selecione um numero')

if num1 > num2:
    if num1 > num3:
       print('o primeiro numero é o maior')
    elif num3 > num2:
        print('o terceiro é o maior')
elif num2 > num3:
    if num2 > num1:
        print('o segundo numero é o maior')
  
