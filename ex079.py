'''Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado.No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
c = ''
list = []
while c in 'S':
	num = int(input('Digite um valor para salvar: '))
	while num in list:
		print(f'O valor {num} já existe na lista.')
		num = int(input('Por favor, digite outro valor para salvar: '))
	list.append(num)
	print(f'Valor {num} salvo com sucesso!!!')
	c = str(input('Deseja continuar [S/N]? ').upper()[0])
	while c not in 'SN':
		print('Por favor, digite a opção correta.')
		c = str(input('Deseja continuar [S/N]? ').upper()[0])
list.sort()
print(f'Os elementos digitados foram:\n{list}')
print('{:*^30}'.format('FIM DO PROGRAMA'))
