'''Faça um programa que leia o nome e o peso de várias pessoas, guardado tudo
em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.'''
dados = []
temp = []
maior = 0
menor = 0
c = 'S'
print('<>' * 30)
print('Bem vindo(a) ao PESOLINO')
while c in 'S':
	temp.append(str(input('Digite o 1º nome: ').strip().title()))
	temp.append(eval(input('Digite o peso em Kg: ')))
	dados.append((temp[:]))
	temp.clear()
	print(f'Cadastro efetuado com sucesso!')
	c = str(input('Deseja cadastar outra pessoa [S/N]? ')).strip().upper()[0]
	while c not in 'SN':
		print('Por favor, digite a opção correta.')
		c = str(input('Deseja cadastrar outra pessoa [S/N]? ')).strip().upper()[0]
print(f'Foram cadastrada(s) {len(dados)} pessoa(s), sendo elas:')
for i in range(0, len(dados)):
	print(f'{dados[i][0]}...', end=' ')
print(f'\nAs pessoa(s) que possui(em) o(s) maiores pesos são:')
# for p in range(len(dados):
#	if dados[p]:

