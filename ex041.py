'''A confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JUNIOR;
- Até 20 anos: SÊNIOR;
- Acima MASTER'''
from time import sleep
from datetime import date
print('''Olá, seja bem-vindo(a)!
Esse programa irá calcular a categoria em
que o aluno pertence, de acordo com sua idade.
Então vamos lá!''')
nome = str(input('Digite o nome do aluno:\n--> ')).title()
nasc = int(input('Digite o ano de nascimento de {}:\n--> '.format(nome)))
idade = date.today().year - nasc
print('CALCULANDO')
sleep(2)
if idade >= 3 and idade <= 9:
    print('A categoria que {} pertence é a MIRIM.\n{} tem {} anos.'.format(nome, nome, idade))
elif idade > 9 and idade <= 14:
    print('A categoria que {} pertence é a INFANTIL.\n{} tem {} anos.'.format(nome, nome, idade))
elif idade > 14 and idade <= 19:
    print('A categoria que {} pertence é a JUNIOR.\n{} tem {} anos.'.format(nome, nome, idade))
elif idade > 19 and idade <= 20:
    print('A categoria que {} pertence é a SÊNIOR.\n{} tem {} anos.'.format(nome, nome, idade))
elif idade > 20:
    print('A categoria que {} pertence é a MASTER.\n{} tem {} anos.'.format(nome, nome, idade))
else:
    print('{} NÃO POSSUI IDADE suficiente para enquadrar em nenhuma categoria.\nEle possui {} ano(s).'.format(nome, idade))
