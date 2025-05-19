

quantidade = 0
valor_total = 0
    
while True:
    print('1 - adicione valor das despesas')
    print('2 - exibir valor total das contas')
    print('0 - Sair')
    opcoes = int(input('Escolha uma das opcoes'))
    if opcoes == 1:
        despesa = int(input('Selecione o valor das despesas'))
        print('O valor de sua despensa foi guardada')
        quantidade += 1
        valor_total += despesa
    elif opcoes == 0:
        print('Secao finalizada')
        break
    elif opcoes == 2:
        print('O valor total se suas despesas é', valor_total)
        print('A quanidade total é de', quantidade)
           
            
            

        
        
        
        