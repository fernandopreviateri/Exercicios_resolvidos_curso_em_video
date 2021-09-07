#Faça um programa que leia a largura e a altura  de uma parede em metros;
#Calcule sua área e a quantidade de tinta necessária para pinta-lá, sabendo
#que cada litro de tinta pinta uma área de 2m².
lar = eval(input('Digite a largura da parede: '))
alt = eval(input('Digite a altura da parede: '))
print('A área da parede é {:.2f}m²\nSão necessários {:.1f}L de tinta.'.format((lar*alt), (lar*alt/2)))
