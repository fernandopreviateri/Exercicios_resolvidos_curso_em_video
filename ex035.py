'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formarem um triângulo'''
seg1 = eval(input('Digite o 1º segmento: '))
seg2 = eval(input('Digite o 2º segmento: '))
seg3 = eval(input('Digite o 3º segmento: '))
if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg2 + seg1):
    print('As retas FORMAM UM TRIÂNGULO.')
else:
    print('As retas NÃO FORMAM UM TRIÂNGULO.')

