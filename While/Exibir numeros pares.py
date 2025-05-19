num = int(input('Digite um numero'))
num1 = 0
while True:
    print(num)
    num -= 2
    num1 += 1
    if num < 0:
        print('A quantidade é de', num1,'pares')
        break