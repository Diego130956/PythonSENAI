ano = int(input('Selecione o ano de nascimento'))

idade = 2025 - ano
 
if idade > 18:
    exibir = 'Maior de idade'
    
elif idade < 18:
        exibir = 'Menor de idade'
        
        
print(exibir)