import inputs
lista_nome = []
while True:
    print('Cadastrar nomes')
    print('1 - Cadastrar nome')
    print('2 - Exibir a quantidade total de nomes')
    print('3 - Exibir os nomes em ordem alfabetica')
    print('4 - Consulta de nomes')
    opcoes = inputs.input_int('Ecolha uma das opcoes:')
    if opcoes == 1:
        nome = inputs.input_str('Qual o seu nome:')
        if nome in lista_nome:
            print('Seu nome ja esta na lista')
        else:
            lista_nome.append(nome)
            print('Nome cadrstado')
    if opcoes == 2:
        nomes2 = len(lista_nome)
        print('Quantidade de nome:', nomes2)
    if opcoes == 3:
        for item in sorted(lista_nome):
            print(item)

    if opcoes == 4:
        verificar = inputs.input_str('Digite o nome q vc deseja encontrtar')
        if verificar in lista_nome:
            print('Nome encontrado!')
            print('Deseja reita-lo da lista?')
            print('1 - Sim')
            print('2 - Não')
            retirar = inputs.input_int()
            if retirar == 1:
                lista_nome.remove(verificar)
                print('Nome removido com sucesso')
            else:
                print('Sessão encerrada')
        else:
            print('Nome não encontardo!')
            print('Deseja adicionar na lista?')
            print('1 - Sim')
            print('2 - Não')
            adicionar = inputs.input_int()
            if adicionar == 1:
                lista_nome.append(verificar)
                print('Nome adicionado com sucesso')
            else:
                print('Sessão encerrada')
