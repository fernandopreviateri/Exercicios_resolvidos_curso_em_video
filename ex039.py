'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo de alistamento.
Seu programa também deverá mostar o tempo que falta
ou que passou do prazo.'''
from datetime import date
print('-=' * 34, '''
Olá JOVEM!
Bem vindo ao programa de verificação de ALISTAMENTO MILITAR.
Para podermos verificar, por favor, digite H para Homem ou M para Mulher: ''')
sexo = str(input('--> '))
ano = date.today().year
if sexo == 'H' or sexo == 'h':
    nasc = int(input('Digite o ano de nascimento --> '))
    if (ano - nasc) > 18:
        print('JOVEM, você já passou do tempo de alistar-se.\nSua idade é de {} anos.'.format(ano - nasc))
        print('Já se passaram {} ano(s) do alistamento.'.format((ano - nasc) - 18))
    elif (ano - nasc) < 18:
        print('JOVEM, ainda não é tempo de alistar-se.\nSua idade é de {} anos.'.format(ano - nasc))
        print('Ainda falta(m) {} ano(s) para o alistamento.'.format(18 - (ano - nasc)))
    else:
        print('JOVEM, a hora é AGORA. Aliste-se.\nSua idade é de {} anos.'.format(ano - nasc))
elif sexo == 'M' or sexo == 'm':
    print('Você é mulher, o alistamento não é obrigatório.')
else:
    print('Digite corretamente!\nTente novamente.')
print('-=' * 34)
