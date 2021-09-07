'''Crie um programa onde o usuário possa digitar sete valores numérios
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em valores crescentes.'''
list = [[], []]
num = 0
for i in range(1, 8):
	num = int(input(f'Digite o {i}º número: '))
	if num % 2 == 0:
		list[0].append(num)
	else:
		list[1].append(num)
	i += 1
list[0].sort()
list[1].sort()
print(f'Os números pares são: {list[0]}\nOs números ímpares são: {list[1]}')
