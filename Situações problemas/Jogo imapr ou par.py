import random

def jogo_imaparpar():
    print('Par ou Impar')
    print('escolha se vc deseja ser par ou impar')
    print('1 - Impar')
    print('2 - Par')
    escolha = int(input('Digite uma das opcoes para o jogo'))
    if escolha == 1:
        print('voce vai ser impar')
        
    elif escolha == 2:
        print('voce vai ser par')
        
    print('Agora escolha o seu numero')
    jogador = int(input(''))
    n_aleatorio = random.randint(1,10)
    print('A maquina escolheu',n_aleatorio)
    total = n_aleatorio + jogador
    total2 = total % 2 == 0
 
 
    if escolha == 1:
        if total2:
            print('Voce perdeu,deseja jogar denovo?')
        else:
            print('Voce ganhou,deseja jogar denovo?')
    if escolha == 2:
        if total2:
            print('voce ganhou,deseja jogar denovo?')
        else:
            print('Voce perdeu, deseja jogar denovo?')
    print('1 - Sim')
    print('2 - Não')
    num = int(input(''))
    if num == 1:
        (jogo_imaparpar)
    else: 
        ('O jogo acabou!')
        




jogo_imaparpar()
        
