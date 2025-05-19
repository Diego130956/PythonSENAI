# Criar uma variavel com uma lista de tres intens

listas = ['caneta', 'lapis', 'apontador', 'oculos', 'borracha']
print('Lista de objetos:', listas)
#Adicionar mais um tem
listas.append('estojo')

#Acessar os objetos em suas devidas posições
print('Objetos em suas posicoes:', listas[0])

#remover um objeto da lista e exibir
obj = listas.pop(1)
print('Objeto removido:', obj)

#Exibir o tamanho da lista
obj2 = len(listas)
print('Quantidadede objetos:', obj2)

#Exibir os itens com o for
print('Exibir os itens:')
for lista in listas:
    print(lista)

#verificar se o objeto esta na lista, se sim exibir, se não remover
if 'cadeira' in listas:
    listas.remove('cadeira')
    
else:
    listas.append('cadeira')
    
#Ordenar a lista em ordem alfabetica, exibindo o antes e depois
listas.sort()
print('Em ordem:', listas)

#Exibir o primeiro e ultimo objeto
len(listas)
primeiro = listas[0]
ultimo = listas [-1] 

print('Primeiro objeto:', primeiro, ',Ultimo objeto:', ultimo)

#Limapr a lista
listas.clear()
nome = int(input('Qual so seu nome:'))
