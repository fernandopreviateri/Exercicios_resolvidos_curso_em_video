'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.'''
from time import sleep
print(('*' * 15), ('M U L T A R E'), ('*' * 15))
velocidade = eval(input('Digite a velocidade aferida do veículo: '))
print('ANALISANDO')
sleep(3)
if velocidade <= 80:
    print('Veículo dentro do limite de velocidade.')
print('VEÍCULO MULTADO!\nO valor da multa é R$ {:.2f}'.format((velocidade-80)*7.0))
print('*' * 45)



