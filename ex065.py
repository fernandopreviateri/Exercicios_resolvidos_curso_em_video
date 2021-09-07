'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
lista = []
confirma = ''
while confirma != 'N':
    lista.append(eval(input('Digite um número qualquer:\n--> ')))
    confirma = str(input('Deseja continuar S/N?\n--> ')).strip().capitalize()
media = sum(lista) / len(lista)
print('O maior número é o {} e o menor {}\nA média é {:.2f}'.format(max(lista), min(lista), media))
print(lista)
