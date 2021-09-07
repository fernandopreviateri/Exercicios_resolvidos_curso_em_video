'''Crie um programa que leia o ano de nascimento de sete pessoas. No
final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
já são maiores.
Considerar maioridade 21 anos'''
from datetime import date
from time import sleep
ano_atual = date.today().year
maior = 0
menor = 0
count = 0
print('''Para saber a quantidade de pessoas de um grupo
que conquistaram a maioridade.''')
sleep(2)
grupo = int(input('Digite a quantidade de pessoas do grupo:\n--> '))
for c in range(0, grupo):
    count = count + 1
    p1 = int(input('Digite o ano de nascimento da {}ª pessoa:\n--> '.format(count)))
    if ano_atual - p1 >= 21:
        maior = (maior + 1)
    else:
        menor = (menor + 1)
print('{} pessoa(s) é/são maior(es) de idade.\n{} pessoa(s) é/são menor(es) de idade.'.format(maior, menor))
