'''Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.
Exemplo:
Ana Maria de Souza
primeiro: Ana
último: Souza'''

nome = str(input('Digite seu nome completo: ')).strip().title()
nome = nome.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é: {}.\nE seu último nome é: {}.'.format(nome[0], nome[-1]))

