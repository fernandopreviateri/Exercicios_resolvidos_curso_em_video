#Faça um programa que leia algo pelo teclado e mostre na tela o seu
#tipo primitivo e todas as informações possíveis sobre ele.
frase = input('Digite algo: ')
print('O tipo de variável é', type(frase))
print('Só tem espaços?', frase.isspace())
print('É um número?', frase.isnumeric())
print('É alfabético?', frase.isalpha())
print('É alfanumérico?', frase.isalnum())
print('Está em maiúscula?', frase.isupper())
print('Está em minúscula?', frase.islower())
print('Está capitalizada?', frase.istitle())
