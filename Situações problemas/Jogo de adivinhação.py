import random
num_maquina = random.randint(0, 100)

print('Bem-Vindo ao jogo de adivinhação!')
print('Estou pensando em um numero de 0 a 100')
print('Tente adinhivinhar!')
print('Para facilitar irei falar se é menor ou maior')


while True:
    num = int(input('Escolha um numero:'))
    if num > num_maquina:
        print('O numero é menor')
    elif num < num_maquina:
        print('O numero é maior')
    elif num == num_maquina:
        print('Voce ganhou')
                
        print('Deseja jogar denovo?')
        print('1 - Sim')
        print('2 - Não')
        escolha = int(input('Escolha uma das opcoes'))
        if escolha == 1:
            print('O jogo recomeçou!')
            num_maquina = random.randint(0, 100)
        else:
            print('O jogo acabou!')
            break
       
    

