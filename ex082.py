'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
list = []
par = []
imp = []
c = 'S'
while c in 'S':
	num = int(input('Digite o número: '))
	list.append(num)
	if num % 2 == 0:
		par.append(num)
	else:
		imp.append(num)
	c = str(input('Deseja continuar [S/N]? ').strip().upper()[0])
	while c not in 'SN':
		c = str(input(f'Por favor, digite a opção correta.\nDeseja continuar [S/N]? ').strip().upper()[0])
list.sort(), par.sort(), imp.sort()
if len(list) > 0:
	if len(par) == 0:
		print(f'Não foi digitado nenhum elemento par.')
		print(f'A lista com os elementos ímpares: {imp}\nA lista com todos os elementos: {list}')
	elif len(imp) == 0:
		print(f'Não foi digitado nenhum elemento ímpar.')
		print(f'A lista com os elementos pares: {par}\nA lista com todos os elementos: {list}')
	else:
		print(f'A lista com os elementos pares: {par}\nA lista com os elementos ímpares: {imp}\nA lista com todos os elementos: {list}')

