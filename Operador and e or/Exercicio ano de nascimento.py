ano = int(input('Solicite o ano de nascimento'))
idade = 2025 - ano

if ano <= 2024:
    if idade <= 10:
        print('Crianca')
    elif idade >= 11 and idade <= 17:
        print('Adolescente')
    elif idade >= 18 and idade <= 59:
        print('Adulto')
    elif idade < 60:
        print('Idoso')
        
else:
    print('Selecione uma ano menor que o atual')
    
            

