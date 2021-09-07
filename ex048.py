'''Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplo de três e que se encontram no intervalo
de 1 até 500.'''
'''soma = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 == 1:
            soma = (soma + c)
print('A soma total de todos os valores é {}'.format(soma))'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os valores é {}. Todos os termos têm o total de {}.'.format(soma, cont))




