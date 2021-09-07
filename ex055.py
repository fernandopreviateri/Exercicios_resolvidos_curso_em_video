'''Faça um programa que leia o peso de cinco pessoas. No
final, mostre qual foi o maior e o menor peso lidos.'''
list = []
c = 0
for c in range(1, 5+1):
    peso = eval(input('Por favor, digite o peso da {}º pessoa:\n--> '.format(c)))
    list.append(peso)
print('O maior peso digitado foi {:.2f}Kg.'.format(max(list)))
print('O menor peso digitado foi {:.2f}Kg.'.format(min(list)))
