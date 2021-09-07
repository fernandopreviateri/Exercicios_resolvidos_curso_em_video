'''Crie um programa que tenha uma tupla única com nome de produtos e
seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
produtos = ('arroz', 10.50,
			'feijão', 8.00,
			'carne', 25.90,
			'shampoo', 6.89,
			'sabonete', 0.50,
			'condicionador', 8.89)
print('*' * 38)
print('{:^40}'.format(' LISTAGEM DE PREÇOS '))
for item in range(0, len(produtos)):
	if item % 2 == 0:
		print(f'{produtos[item]:.<29}'.title(), end =' ')
	else:
		print(f'R${produtos[item]:>6.2f}')
print('*' * 38)