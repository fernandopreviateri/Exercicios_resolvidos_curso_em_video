#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímitros.
n = eval(input('Bem-vindo(a) ao programa conversor!\nPor favor, digite o valor em metro para ser convertido: '))
print('{:.3f} km\n{} hm\n{} dam\n{} m\n{} dm\n{} cm\n{} mm'.format((n/1000),(n/100), (n/10), (n), (n*10), (n*100), (n*1000)))



