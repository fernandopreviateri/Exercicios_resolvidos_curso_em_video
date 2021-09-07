'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto'''
from datetime import date
from time import sleep
print(('*' * 10), ('BISSEXTO 1.0'), ('*' * 10))
ano = int(input('Digite o ano que quer analisar? Ou precissione 0 para analizar o atual: '))
print('ANALISANDO')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} é um ano comum.'.format(ano))
