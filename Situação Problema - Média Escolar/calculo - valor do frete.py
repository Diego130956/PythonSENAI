print('Vamos calcular valor do frete')
def calcular_frete(peso, distancia, taxa_fixa):
    valor = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    print('O valor do frete sera de', valor, 'reais')
    
    
    
    
peso = int(input('qual o peso do pacote'))
distancia = int(input('qual a distancia percorrida'))
taxa_fixa = int(input('qual a taxa fixa da entrega'))
calcular_frete(peso, distancia, taxa_fixa)