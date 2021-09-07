'''Crie um programa que irá gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem dos números gerados e também indique o menor
e o maior valor que estão na tupla.'''

from random import randint
gerador = (randint(1, 20), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10, ))
print(f'Os números sorteados foram: {gerador}\nO maior número é {max(gerador)}\nO menor número é o {min(gerador)}')

