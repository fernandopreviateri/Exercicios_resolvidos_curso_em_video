'''Escreva um programa que leia um número inteiro qualquer
e peça ao usuário escolher qual a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''
from time import sleep
num = int(input('Digite um número: '))
base = int(input('Para fazer a conversão:\nDigite 1 p/ binário\nDigite 2 p/ octal\nDigite 3 p/ hexadecimal\n-> '))
print('C O N V E R T E N D O')
sleep(4)
if base == 1:
    print('{} convertido p/ binário é igual a {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido p/ octal é igual a {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido p/ hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
