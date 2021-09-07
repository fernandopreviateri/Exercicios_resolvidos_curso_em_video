'''Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna;
c) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = soma = 0
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}]', end = '')
		if matriz[l][c] % 2 == 0:
			pares += matriz[l][c]
	print()
print('-=' * 30)
print(f'A soma dos valores pares é: {pares}.')
for l in range(0, 3):
	soma += matriz[l][2]
print(f'A soma da 3ª coluna é : {soma}.')
for c in range(0, 3):
	if c == 0 or matriz[1][c] > maior:
		maior = matriz[1][c]
print(f'A soma da 2ª linha é: {maior}.')
