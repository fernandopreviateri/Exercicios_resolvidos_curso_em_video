'''Faça um programa que mostre na tela uma contagem regressiva para o
estouro dos fogos de artifício, indo de 10 até 0, com uma pausa de 1
segundo entre eles.'''
print('{:.^36}'.format('C O N T A G E M  R E G R E S S I V A'))
from time import sleep
sleep(1.5)
for c in range(10, -1, -1):
    print('-->', c)
    sleep(1)
print('{:.^9} FELIZ ANO NOVO!!! {:.^9}'.format('', ''))
