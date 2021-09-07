'''Crie um programa que leia o nome e o preço de vários produtos. O
programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra;
b) Quantos produtos custam mais de R$ 1000;
c) Qual o nome do produto mais barato.'''
mais1000 = cont = menor = total = 0
barato = ' '
while True:
	produto = str(input('Digite o nome do produto: ')).strip().title()
	preco = eval(input('Digite o preço do produto em R$: '))
	resp = ' '
	total += preco
	cont += 1
	if preco > 1000:
		mais1000 += 1
	if cont == 1 or preco < menor:
		menor = preco
		barato = produto
	while resp not in 'SN':
		resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
	if resp == 'N':
		break
print('{:*^30}'.format(' FIM '))
print(f'''O total da compra é de R$ {total:>14.2f}
{mais1000} produto(s) custa mais de R$ {'1000,00':>10}
{barato} é o produto mais barato.''')
'''Isso é só um exemplo'''