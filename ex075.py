'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.'''
tupla = (eval(input('Digite o 1º número: ')), eval(input('Digite o 2º número: ')), eval(input('Digite o 3º número: ')), eval(input('Digite o 4º número: ')))
print(f'O número 9 apareceu {tupla.count(9)} vez(es).')
if 3 in tupla:
	print(f'O número 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
	print(f'O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram:', end=' ')
for i in tupla:
	if i % 2 == 0:
		print(i, end=' ')
