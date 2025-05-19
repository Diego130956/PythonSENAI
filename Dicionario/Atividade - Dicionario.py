jogo1 = {
    'nome':'Free Fire',
    'objetivo':'sobrevivencia',
    'Persogem principal':'Adam e Eve',
    'classificacao de idade': '13 anos'
}

jogo2 = {
    'nome':'Brawl Stars',
    'objetivo':'Batalhar',
    'Persogem principal':'Shelly',
    'Classificacao de idade': 'livre'
        
}
jogo3 = {
    'nome':'Clash Royale',
    'objetivo':'destricao',
    'Persogem principal':'O rei',
    'Classificacao de idade': 'livre'
    
}
#Exibir uma lista de Dicionarios

lista_jogos = [jogo1, jogo2, jogo3]
    #Escolhendo os campos
for jogo in lista_jogos:
    print(f"{jogo['nome']}")
    #Exibindo todos
    
for jogo in lista_jogos:
    for chave, valor in jogo.items():
         print(f'{chave}: {valor}')
    print()
