''' Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas;
-> O nome com todas as letras minúsculas;
-> Quantas letras ao todo (sem considerar espaços);
-> Quantas letras tem o primeiro nome '''

nome = str(input('Digite seu nome completo: ')).strip()
print('1º - As letras do seu nome em maiúsculas ficam assim: {}'. format(nome.upper()))
print('2º - As letras do seu nome em minúsculas ficam assim: {}'. format(nome.lower()))
print('3º - Seu nome possui: {} letras.'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('4º - Seu primeiro nome possui {} letras.'.format(len(nome[0])))
