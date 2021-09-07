'''Crie um programa que leia o nome de uma pessoa
e diga se ela tem Silva no nome.'''
nome = str(input('Digite seu nome completo: ')).strip().upper().split()
print('A afirmação de que seu nome possui SILVA é: {}'.format('SILVA' in nome))
