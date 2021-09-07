#Faça um programa que leia um ângulo qualquer e mostre na tela o
#valor do seno, cosseno e tângente desse ângulo.
from math import cos, sin, tan, radians
ang = eval((input('Digite o ângulo: ')))
print('O seno deste ângulo é {:.2f}\nO cosseno deste ângulo é {:.2f}\nE a reta tangente é {:.2f}'.format(sin(radians((ang))), (cos(radians(ang))), (tan(radians(ang)))))

