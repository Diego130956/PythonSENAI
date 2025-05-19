def resultado(num1, num2):
        
    print('Soma:', adicao(num1, num2))
    print('Multiplicacao:', multiplicacao(num1, num2))
    print('Divisao:', divisao(num1, num2))
    print('Subtracao:', subtracao(num1, num2))


def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def adicao(num1, num2):
    return num1 + num2
def divisao(num1, num2):
    return num1 / num2

def menu_operacao(num1, num2):
    
            print('Escolha uma operacao')
            print('1 - Soma')
            print('2 - Divisao')
            print('3 - Subtracao')
            print('4 - Multiplicacao')
            print('5 - todas as operacoes')
            while True:
                operacao = int(input('Escolha uma das operacoes exibidas'))
                if operacao == 1:
                    print(adicao(num1, num2))
                elif operacao == 2:
                    print(divisao(num1, num2))
                elif operacao == 3:
                    print(subtracao(num1, num2))
                elif operacao == 4:
                    print(multiplicacao(num1, num2))
                elif operacao == 5:
                    print(resultado(num1, num2))
                else:
                    print('Escolha um dos numeros solicitados')
                break
                       
        
while True:
    try:
        num1= float(input('Digite um numero'))
        break
    except ValueError:
            print('Digite apenas numeros, EX:(20)')
while True:
    try:
        num2 = float(input('Digite outro numero'))
        break
    except ValueError:
        print('Digite apenas numeros, EX:(10)')
    
    
menu_operacao(num1, num2)

 
            
        
        
            
            