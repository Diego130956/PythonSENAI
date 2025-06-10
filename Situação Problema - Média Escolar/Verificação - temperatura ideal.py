print('Vamos verificar se a temperatura esta ideal ou nao')
def verificar_temperaturaideal(temperatura, umidade, escolha):
    if escolha == 'inverno':
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and umidade <= 55:
                print('A qualidade do ar esta ideal para o inverno')
        else:
            print('A qualidade do ar esta inadequada')
    elif escolha == 'verao':
        if temperatura >= 23 and temperatura <= 26:
            if umidade >= 56 and umidade <= 65:
                print('A qualidade do ar esta ideal para o verao')
        else:
            print('A qualidade do ar esta inadequada')
    
        
        
        
escolha = str(input('Escolha a estacao inverno ou verao'))
temperatura = int(input('Digite a temperatura'))
umidade = int(input('Agora digite a umidade'))
verificar_temperaturaideal(temperatura, umidade, escolha)
