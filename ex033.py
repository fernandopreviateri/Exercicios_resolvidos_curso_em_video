'''Faça um programa que leia três números e mostre qual é
o menor e qual é o maior número digitado'''
from time import sleep
print('-=' * 10, 'D I G I T A D O R ', '-=' * 10)
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
print('PROCESSANDO')
sleep(3)
print('O maior número é o {}.\nE o menor número é o {}.'.format(max(num1, num2, num3), min(num1, num2, num3)))
print('-=' * 30)

