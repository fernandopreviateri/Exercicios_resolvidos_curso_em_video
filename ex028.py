'''Escreva um programa que faça o computador pensar em um número inteiro
entre 0 e 5 e peça ao usuário tentar descobrir qual foi o número escolhido
pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 30)
name = str(input(('Qual é o seu nome? ')))
print('{}, seja bem vindo(a)'.format(name))
print('-=-' * 30)
q = int(input('{} tente advinhar um número que pensei de 0 a 5: '.format(name)))
print('PROCESSANDO')
sleep(3)
if q == n:
    print('Parabéns {}\nVocê venceu!!!\nEscolhi exatamente o número: {}'.format(name, n))
else:
    print('{}, você perdeu!'.format(name))
    print('Escolhi o número: {}'.format(n))



