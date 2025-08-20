'''
crie um programa que leia numeros inteiros e
substitua o maior pela diferencia e escreva ambos no console
'''

num1 = 10
num2 = 8

while num1 != num2:
    
    if num1 > num2:
        diferenca = num1 - num2
        num1 = diferenca

    elif num2 > num1:
        diferenca = num2 - num1
        num2 = diferenca

print(f'mdc: {num1}')



'''
10
8

10 - 8 = 2

2
8

8 -2 = 6
2
6

6 - 2 = 4

2
4

4 - 2 = 2

2
2
'''