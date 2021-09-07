'''Faça um programa que leia um número qualquer e mostre o seu fatorial
Ex: 5! = 5x4x3x2x1 = 120'''
num = int(input('Digite um número para ser fatoriado:\n--> '))
cont = num
print('Calcular {}! = '.format(num))
f = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))
