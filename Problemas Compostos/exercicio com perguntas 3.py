#Passo a Passo

#1 O valor necesario para completar o tanque

#2 Quantos litros falta para completar o tanque e o valor do litro da combustivel

#3
#Passo1 Subtrair a capcidade total de litros pela quantidade atual
#Passo2 Multiplicar o valor encontrado pelo custo do combustivel por litro
#Passo3 Exibir o resultado

tanque = int(input('Qual a capacidade total em litros?'))
tanque1 = float(input('Quantos litros deseja colocar?'))
total = tanque - tanque1

preco = float(input('Qual o valor do combustivel por litro?')) 
print('o valor total para encher o tanque é', total * preco, 'reais')

