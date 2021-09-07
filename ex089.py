'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita que
o usuário possa mostrar as notas de cada aluno individualmente.'''
from time import sleep
temp1 = []
list = []
c = 'S'
print('<<>>' * 9)
print('{:^30}'.format('ESCOLARE'))
print('{:^30}'.format('CALCULADOR DE MEDIA'))
print('<<>>' * 9)
while c in 'S':
	nome = str(input('Digite o primeiro nome do aluno(a):\n')).strip().lower().title()
	n1 = eval(input('Digite a 1ª nota: '))
	n2 = eval(input('Digite a 2ª nota: '))
	media = (n1 + n2) / 2
	temp1.append(nome)
	temp1.append(n1)
	temp1.append(n2)
	temp1.append(media)
	list.append(temp1[:])
	temp1.clear()
	c = str(input('Deseja cadastrar novo aluno(a) [S/N]? ')).strip().upper()[0]
	while c not in 'SN':
		c = str(input('Por favor, digite a opção correta.\nDeseja cadastar novo aluno [S/N]? ')).strip().upper()[0]
a = 0
while 0 <= a <= 2:
	cont = 1
	if a == 0:
		print('<<>>' * 9)
		print('{:^30}'.format('LISTA COMPLETA'))
		print('{:<30}'.format('NOME'), end=' ')
		print('MEDIA')
		print('-' * 36)
		for i in range(0, len(list)):
			print(f'{list[i][0]:<10}{list[i][cont]:>26.1f}')
			cont += 1
			sleep(0.5)
	elif a == 1:
		print('-' * 36)
		print(f'{"Nº":<4}{"NOME":<12}')
		for f, a in enumerate(list):
			print(f'{f:<4}{a[0]:<10}')
		while True:
			mostrar = int(input('Digite o nº correspondente ao aluno\npara mostrar as notas [999 - VOLTA]:  '))
			if mostrar == 999:
				break
			if mostrar <= len(list) - 1:
				sleep(0.5)
				print(f'As notas de {list[mostrar][0]} são {list[mostrar][1]} e {list[mostrar][2]}.')
				print('-')
	elif a == 2:
		break
	else:
		print('Por favor, digite a opção correta.')
	print('-' * 36)
	a = int(input('Digite a opção desejada:\nOpção 0: Exibir boletim novamente.\nOpção 1: Exibir notas individualmente.\nOpção 2: Sair do programa.\n--> '))
print('{:-^36}'.format(' FIM DO PROGRAMA '))

