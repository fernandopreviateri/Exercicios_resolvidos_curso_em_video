'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 Km
e R$ 0,45 para viagens mais longas.'''
from time import sleep
print('*' * 10, ('PASSAGEM FÁCIL'), ('*' * 10))
dist = eval(input('Qual é a distância em km para seu destino? '))
print('PROCESSANDO . . .')
sleep(2)
if dist <= 200:
    print('O preço da passagem é R$ {:.2f}'.format(dist * 0.50))
else:
    print('O preço da passagem é R$ {:.2f}'.format(dist * 0.45))
print('*' * 36)

