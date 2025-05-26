import inputs
lista_livros = []

while True:
    try:
    
        print("Bem-Vindo ao cadastro de livros")
        print("1 - Cadastrar os livros")
        print("2 - Livros cadastrados")
        print("3 - Quantidade de livros")
        print("4 - livro de um autor expecifico")
        print("5 - Buscar livro por categoria")
        print("6 - Editar dados de um livro")
        escolha = inputs.input_int('Escolha uma das opcoes')
        if escolha == 1:

            isbn = inputs.input_int("Digite o isbn do livro")
            titulo = inputs.input_str("Digite o titulo do livro")
            autor = inputs.input_str("Digite o autor do livro")
            categoria = inputs.input_str("Qual a categoria do livro")
            ano_publicacao = inputs.input_int("Qual o ano de sua publicacao")
                
            lista_livros.append({
                "isbn":isbn,
                "titulo":titulo,
                "autor":autor,
                "categoria":categoria,
                "ano":ano_publicacao
            })
            print('Adicionado')
        elif escolha == 2:
            for ordem in lista_livros:
                print('ISBN -', f"{ordem['isbn']}")
                print('Titulo -', f"{ordem['titulo']}")
                print('Autor -', f"{ordem['autor']}")
                print('Categoria -', f"{ordem['categoria']}")
                print('Ano -', f"{ordem['ano']}")

        elif escolha == 3:
            livros2 = len(lista_livros)
            print('Quantidade de livros:', livros2)
            
        elif escolha == 4:
            verificar = inputs.input_str('Digite o autor que voce deseja encontar')
            for verificar2 in lista_livros:
                if verificar2['Autor'] == verificar:
                    print(f"Titulo - {verificar2['Titulo']}")
        elif escolha == 5:
            categoria_livro = inputs.input_str('Digite a categoria do livro')
            for categorias in lista_livros:
                if categorias['Categoria'] == categoria_livro:
                    print(f"Titulo - {categorias['Titulo']}")
        elif escolha == 6:
            editar_dados = inputs.input_int('Digite o do ISBN do livro')
            for edicao in lista_livros:
                if edicao['ISNB'] == editar_dados:
                    titulo = inputs.input_str('Digite o nome do livro')
                    autor = inputs.input_str('Digite o autor do livro')
                    categoria = inputs.input_str('Digite a categoria ')
                    ano = inputs.input_int('Digite o ano')
                    edicao['titulo'] = titulo
                    edicao['autor'] = autor
                    edicao['categoria'] = categoria
                    edicao['ano'] = ano
                    print('Dados atualizados')
                    break 
                else:
                    print('Livro nao encontrado')
    except ValueError:
        print("")
    
        
        
        
        
        
        
        
        
        
    
        
