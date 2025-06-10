print('Vamos calcular o tempo do percurso')
def calcular_tempo(distancia, velocidade):
    calculo = distancia/velocidade
    print('O tempo é de', calculo,'horas')
    
    
distancia = int(input('Digite a distancia'))
velocidade = int(input('Digite a velocidade'))
calcular_tempo(distancia, velocidade)
    