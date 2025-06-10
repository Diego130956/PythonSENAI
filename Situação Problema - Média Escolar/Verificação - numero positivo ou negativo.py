print('Escolha um numero positivo ou negativo')
def verificar_numero(num):
   
    if num > 0:
        print('Numero positivo')
        return True 
    else:
        print('Numero negativo')
        return False
    
num = int(input(''))
verificar_numero(num)