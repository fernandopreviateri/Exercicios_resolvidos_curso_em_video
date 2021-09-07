'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
from time import sleep
termo1 = eval(input('Digite o 1º termo:\n--> '))
sleep(0.5)
print('Ok!')
sleep(0.5)
r = eval(input('Digite a razão:\n--> '))
decimo = termo1 + (10 - 1) * r
for c in range(termo1, decimo + r, r):
    print('{}'.format(c), end='--> ')
print('acabou')

