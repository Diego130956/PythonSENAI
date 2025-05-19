from datetime import datetime


def hour(nome):
    print('Hora', datetime.now().hour)
    hour = datetime.now().hour
    if hour >= 0 and hour <= 5:
        print('Boa Madrugada',nome)
    elif hour >= 5.01 and hour <= 12:
        print('Bom Dia', nome)
    elif hour >= 12.01 and hour <= 19:
        print('Boa Tarde', nome)
    elif hour >= 19.01 and hour <= 23.59:
        print('Boa Noite', nome)
        
        
nome = input('Digite o seu nome')


hour(nome)

