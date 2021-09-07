'''Crie um programa que leia um número inteiro
e mostre na tela se ele é par ou ímpar'''
from time import sleep
print('*' * 10, 'PAR OU ÍMPAR', '*' * 10)
num = int(input('Digite um número: '))
print('PENSANDO NISSO . . .')
sleep(3)
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O numéro {} é ímpar!'.format(num))
print('*' * 34)
