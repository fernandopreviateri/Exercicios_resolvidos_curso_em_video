'''Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).'''
cont = total = user = 0
while user != 999:
    user = int(input('Digite um número inteiro:\n[999 para]--> '))
    if user != 999:
        total += user
        cont = cont + 1
print('Foram digitados {} números e a soma deles é igual a {}'.format(cont, total))
