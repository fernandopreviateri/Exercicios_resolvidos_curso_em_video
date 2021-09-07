'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O
programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
print('<<>>' * 12)
print('{:^43}'.format(' PALPITEIRO '))
print('<<>>' * 12)
jogos = int(input('Digite o número de jogos para eu palpitar à você: '))
list = []
temp = []
total = 1
while total <= jogos:
	cont = 0
	while True:
		j = randint(1, 60)
		if j not in temp:
			temp.append(j)
			cont += 1
		if cont >= 6:
			break
	list.append(temp[:])
	temp.clear()
	total += 1
cont1 = 1
for c in range(0, len(list)):
	list[c].sort()
	sleep(0.5)
	print(f'{cont1:>2}º jogo: {list[c]}')
	cont1 += 1
print('<<>>' * 12)