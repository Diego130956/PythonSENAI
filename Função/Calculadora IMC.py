def calcula_imc(altura, peso):
    resultado = peso / (altura * altura)
    return resultado

def classifica_imc(imc):
    if imc < 18.5:
        print('Magresa')
    elif imc >= 18.5 and imc <= 24.9:
        print('Peso normal')
    elif imc >= 25 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30 and imc <= 34.9:
        print('Obesidade grau I')
    elif imc >= 35 and imc <= 39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade grau III')
    
    
    
altura = float(input('Digite uma altura'))
peso = float(input('Digite o peso'))
imc = calcula_imc(altura, peso)
classifica_imc(imc)
