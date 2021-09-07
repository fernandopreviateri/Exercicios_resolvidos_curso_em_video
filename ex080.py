'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
um uma lista, já na posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
list = []
cont = 1
for i in range(1, 6):
	num = int(input(f'Digite o {cont}º número: '))
	if i == 0 or num > list[-1]:
		list.append(num)
		print(f'Adicionado no final da lista...')
	else:
		pos = 0
		while pos < len(list):
			if num <= list[pos]:
				list.insert(pos, num)
				print(f'Adicionado na posição {pos} da lista...')
				break
			pos += 1
	cont += 1
print(f'Os valores ordenados são: {list}')


