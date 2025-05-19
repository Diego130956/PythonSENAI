#Passo a Passo

#1 Quantos reais e litros de combustivel é necessario para fazer a viagem

#2 Os quilometros rodado pelo carro
#  o valor do combustivel
#  a autonomia do carro por litro
#  quantia de litro restante dentro do tanque

#3
#Passo1 Subtrair os quilometros e dividir pela autonomia do carro
#Passo2 Subtrair o resultado pela quantia de combustivel restante
#Passo3 Multiplicar o ultimo resultado pelo valor do combustivel por litro
#Passo4 Exibir os resultados

quilometro = 800 - 90
litro = float(quilometro / 7)

preco = float(litro - 10)
preco1 = preco * 6.90
print('seu gasto vai ser no total de', preco1,'reais')
print('é necessario', preco,'litros de combustivel para a viagem inteira')
