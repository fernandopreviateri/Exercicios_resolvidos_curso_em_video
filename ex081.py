'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o nº 5 foi digitado e está ou não na lista.'''
list = []
c = 'S'
while c in 'S':
	list.append(int(input('Digite o número: ')))
	c = str(input(f'Deseja conitnuar [S/N]? ').strip().upper()[0])
	while c not in 'SN':
		c = str(input(f'Por favor, escolha a opção correta.\nDeseja continuar [S/N]? ').strip().upper()[0])
print(f'Foram digitados {len(list)} elemento(s).')
list.sort(reverse=True)
print(f'Ordenados na forma decrescente são: {list}')
#for i in range(0, len(list)):
if 5 not in list:
	print(f'O número 5 não foi encontrado na lista!')
else:
	print(f'Número 5 foi encontrado na lista')
