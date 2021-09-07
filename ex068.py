'''Faça um programa que jogue par ou ímpar com o cpu. O jogo só
sera interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo'''
from time import sleep
from random import randint
cont = 0
print(f'*' * 15, 'GAME PAR OU ÍMPAR', '*' * 15)
while True:
	you = str(input('Escolha:\n* P para PAR\n* I para ÍMPAR --> ')).strip().upper()[0]
	while you not in 'PI':
		print('Por favor, digite corretamente.')
		you = str(input('Escolha:\n* P para PAR\n* I para ÍMPAR --> ')).strip().upper()[0]
	n = int(input('Digite um número --> '))
	c = randint(0, 10)
	total = n + c
	for i in range(1, 4):
		print(i, '-->', end=' ')
		sleep(1.0)
	print('JÁ!')
	sleep(1)
	if you == 'P':
		if total % 2 == 0:
			print(f'VOCÊ GANHOU!\nO PC escolheu {c} e você {n}, que deu o total de {total}; é PAR!')
			cont += 1
		else:
			print(f'VOCÊ PERDEU !!!\nO PC escolheu {c} e você {n}, que deu o total de {total}; é ÍMPAR!')
			break
	elif you == 'I':
		if total % 2 == 1:
			print(f'VOCÊ GANHOU!\nO PC escolheu {c} e você {n}, que deu o total de {total}; é ÍMPAR!')
			cont += 1
		else:
			print(f'VOCÊ PERDEU !!!\nO PC escolheu {c} e você {n}, que deu o total de {total}; é PAR!')
			break
print(f'VOCÊ TEVE {cont} VITÓRIA(S).\nGAME OVER!')
