'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas
posições na lista.'''
list = []
c = ''
while c in 'S':
	for p in range(1, 6):
		list.append(int(input(f'Digite o {p}º número: ')))
		p += 1
	print(f'Os elementos da lista são: {list}')
	print(f'O maior elemento da lista é o {max(list)}.')
	print(f'E está na(s) posição(ões)', end= ' ')
	for i, v in enumerate(list):
		if v == max(list):
			print(f'{i+1}...', end='')
	print()
	print(f'O menor elemento da lista é o {min(list)}.')
	print(f'E está na(s) posição(ões)', end=' ')
	for i, v in enumerate(list):
		if v == min(list):
			print(f'{i+1}...', end='')
	print()
	c = str(input('Deseja continuar [S/N]? ').upper()[0])
	while c not in 'SN':
		c = str(input('Por favor, digite corretamente [S/N]? ').upper()[0])
print('{:-^30}'.format(' FIM DO PROGRAMA '))


