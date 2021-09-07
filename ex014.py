#Escreva um programa que converta uma temperatura digitando graus
#Celsius e converta para graus Fahrenheit.
print('Bem-vindo(a) ao PCT - Programa Conversor de Temperaturas')
cel = eval(input('Digite os graus em ºC '))
print('{:.1f}Cº equivale a {:.1f}Fº'.format(cel, ((cel * 9 / 5) + 32)))
