'''Crie um programa que leia uma frase qualquer e diga se ele é
palíndromo, desconsiderando os espaços.
ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA'''
# 1º - Foi digitada e lida a frase eliminado os espaços de antes / depois e colocado em maiúscula
frase =str(input('Digite uma frase:\n--> ')).strip().upper()
# 2º - Foi usado o split() para que gerasse uma lista
palavras = frase.split()
# 3º - Juntado a lista sem os espaços
junto = ''.join(palavras)
# 4º - Foi transformado em inverso a str
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
# 5º - Comparação
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')



