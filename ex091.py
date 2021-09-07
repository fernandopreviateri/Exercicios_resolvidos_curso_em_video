'''Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
dados = dict()
for i in range(1, 5):
	dados[i] = randint(1, 6)
print('-=' * 15)
for k, v in dados.items():
	print(f'Jogador{k} tirou {v}')
	sleep(1)
classificao = []
classificao = sorted(dados.items(), key=itemgetter(1), reverse= True)
print('*' * 30)
print(f'{" CAMPEÃO ":*^30}')
print('*' * 30)
for i, v in enumerate(classificao):
	print(f"{i + 1}º lugar jogador{v[0]} --> {v[1]} ******")
	sleep(0.5)
print('*' * 30)
