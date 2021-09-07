'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''
from time import sleep
print('*' * 15, 'T A B U A N D O', '*' * 15)
while True:
	n = int(input('Digite um número para ver a Tabuada\n--> '))
	if n < 0:
		break
	print('*' * 30)
	for c in range(1,11):
		produto = n * c
		print('{} X {} = {}'.format(n, c, produto))
		sleep(0.3)
	print('*' * 30)
print('PROGRAMA ENCERRADO')
