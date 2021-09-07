'''Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado(número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('{:*^60}'.format(' BANCO DO POVO '))
valor = int(input('Digite o valor que você quer sacar R$ '))
total = valor
ced = 50
totalced = 0
while True:
	if total >= ced:
		total -= ced
		totalced += 1
	else:
		if totalced > 0:
			print(f'Total de {totalced} cédulas de R$ {ced:.2f}')
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		totalced = 0
		if total == 0:
			break
print('SAQUE EFETUADO COM SUCESSO !')
print('{:*^60}'.format(''))
