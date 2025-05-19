not1 = int(input('Solicite uma nota'))
not2 = int(input('Solicite outra nota'))

med = (not1 + not2) / 2
if not1 > 0 and not1 <= 100 or not2 > 0 and not2 <= 100:
    if med >= 70:
        print('Aprovado')
    elif med >= 50 and med <= 70: 
        print('Recuperacao')
    elif med <= 50:
        print('Reprovado')
        
else:
    print('Digite um numero de 0 a 100')

