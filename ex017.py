#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule e
#mostre o comprimento da hipotenusa.
from math import hypot
cat_opo = eval(input('Digite o comprimento do cateto oposto: '))
cat_adj = eval(input('Digite o comprimento do cateto adjacente: '))
'''hi = (cat_opo ** 2 + cat_adj ** 2) ** (1/2)'''
print('A hipotenusa vai medir {:.2f}.'.format(hypot(cat_opo, cat_adj)))



