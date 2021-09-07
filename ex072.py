'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e vinte)
e mostrá-lo por extenso.'''
from random import randint
list = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
		'seis', 'sete', 'oito', 'nove', 'dez',
		'onze', 'doze', 'treze', 'catorze', 'quinze',
		'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
print('{:-^40}'.format(' PROGRAMA EXTENSIOR '))
print('{:<}Neste programa você digitará um número e\nreceberá ele em forma de extenso no inter-\nvalo de 0 a 20. Vamos lá!'.format(''))
confirm = 'S'
while confirm == 'S':
	n = int(input('Digite o número: --> '))
	while True:
		if 0<= n <= 20:
			break
		else:
			print('Por favor, digite corretamente.')
			n = int(input('Digite o número: --> '))
	print(f'Você digitou o número {list[n].upper()}.')
	print('{:-^40}'.format(''))
	confirm = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
	while confirm not in 'SN':
		print('Por favor, selecione a opção correta.')
		confirm = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
	if confirm == 'N':
		break
	else:
		print('Ótimo. Vamos lá!')
print('Ok. Tenha um bom dia!\n{:-^40}'.format(' FIM DO PROGRAMA '))




