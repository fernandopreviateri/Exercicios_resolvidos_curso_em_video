'''Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre:
--> A média de idade do grupo;
--> Qual o nome do homem mais velho;
--> Quantas mulheres têm menos de 21 anos.'''
from time import sleep
nome = []
idade = []
sexo = []
for c in range(1, 3+1):
    print('------- {}ª pessoa --------'.format(c))
    nome.append(input('Digite o nome:\n--> ').title().strip())
    idade.append(int(input('Digite a idade:\n--> ')))
    sexo1 = str(input('Para masculino digite M:\nPara feminino digite F:\n--> ')).strip()
    if sexo1 == 'M' or sexo1 == 'm':
        sexo.append('masculino')
    elif sexo1 == 'F' or sexo1 =='f':
        sexo.append('feminino')
    else:
        print('Letra INVÁLIDA !!!\nDigite corretamente')
    print('S A L V A N D O'), sleep(1)







media = '{:.2f}'.format((sum(idade)) / len(idade))





