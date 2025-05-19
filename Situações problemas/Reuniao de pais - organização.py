lista_reuniao = []
lista_ausente = []
lista_presente = []

while True:
    print('Reuniao de pais')
    print('1 - Cadastrar nomes')
    print('2 - Exibir toatal de pais')
    print('3 - Lista de nomes em ordem alfabetica')
    print('4 - Confirmação de presença dos pais')
    print('5 - Relatorio de chamada')
    opcoes = int(input('Escolha uma das opcoes:'))
    if opcoes == 1:
        nomes = input('Qual o seu nome:')
        if nomes in lista_reuniao:
            print('Este nome ja esta na lista')
        else:
            lista_reuniao.append(nomes)
            print('Nome cadrstado')
    if opcoes == 2:
        pais = len(lista_reuniao)
        print('Quantidade de nome:', pais)
    if opcoes == 3:
        for ordem in sorted(lista_reuniao):
            print(ordem)
    if opcoes == 4:
        for nome in lista_reuniao:
            print(nome)
            print('1 - SIM')
            print('2 - NÃO')
            presenca = int(input('Esta presnete?'))
            
            if presenca == 1:
                lista_presente.append(nome)
            else:
                lista_ausente.append(nome)
            
            
            
    if opcoes == 5:
        print('Ausentes:')
        for ausentes in sorted(lista_ausente):
            print(ausentes)
        print('Presentes:')
        for presente in sorted(lista_presente):
            print(presente)
            

        
        