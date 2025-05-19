num1 = int(input('Selecione um numero'))
num2 = int(input('Selecione um numero'))

num3 = num1 + num2
num4 = num3 / 2

if num4 > 70:
    exibir = 'aprovado'
    
elif num4 < 70:
    exibir = 'reprovado'
    
print(exibir)