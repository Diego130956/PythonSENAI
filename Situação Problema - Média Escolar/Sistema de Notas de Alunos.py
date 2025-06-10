lista_nomes = []

def Menu():
    print('')
    print('1 - cadastrar nome')
    print('2 - Media do aluno')
    print('3 - Verificar situacao')
    print('4 - Mostar relatorio')




def cadastrar_aluno():
    nome =  str(input('Digite o seu nome:'))
    nota1 = float(input('Digite a primeira nota:'))
    nota2 = float(input('Digite a segunda nota:'))
    nota3 = float(input('Digite a terceira nota:'))
    media = calcular_media(nota1, nota2, nota3)
    situacao = verificar_situacao(media)
    
    aluno = {
        'nome':nome,
        'media':media,
        'situacao':situacao
        }
    lista_nomes.append(aluno)
        
     
def calcular_media(nota1, nota2, nota3):
    conta = nota1 + nota2 + nota3
    media1 = round(conta/3)
    return media1
    
def verificar_situacao(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <= 6.9:
        return 'Recuperacao'
    else:
        return'Reprovado'
    
def mostrar_relatorio(lista_nomes):
    for ordem in lista_nomes:
        print('')
        print('Nome: -', f"{ordem['nome']}")
        print('Media: -', f"{ordem['media']}")
        print('Situacao: -', f"{ordem['situacao']}")
        print('')
        

    

    
    
while True:
    Menu()
    print('')
    opcoes = int(input('Escolha uma das opcoes:'))
    if opcoes == 1:
        
        cadastrar_aluno()
        
    elif opcoes == 2:
        print(calcular_media(nota1, nota2, nota3))
       
    elif opcoes == 3:
        media = calcular_media(nota1, nota2, nota3)
        situacao = verificar_situacao(media)
        print(verificar_situacao(media))

    elif opcoes == 4:
        print(mostrar_relatorio(lista_nomes))
        
            

 

