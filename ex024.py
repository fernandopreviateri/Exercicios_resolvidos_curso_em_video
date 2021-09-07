'''Crie um programa que leia o nome de uma cidade e diga se ela
tem ou não com o nome SANTO'''
city = str(input('Digite a cidade que você nasceu: ')).strip()
city = city.upper()
city = city.split()
print('SANTO' in city)
