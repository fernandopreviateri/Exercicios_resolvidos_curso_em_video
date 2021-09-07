'''Refaça o desafio ex009, mostrando a tabuada
de um número que o usuário escolher, só que
agora utilizando um laço for.'''
from time import sleep
print('''{:^30}
Seja muito bem-vindo(a) ao TABULE.
Aqui, você descobre a tabuada até
o 10 do número inteiro digitado.'''.format(' T A B U L E '))
sleep(1.5)
print('Vamos lá,')
sleep(1.5)
fator1= int(input('Digite um número:\n--> '))
if fator1 > 0:
    print('Ok! Tabuada do {}.'.format(fator1))
    sleep(0.5)
    print('PROCESSANDO . . .')
    sleep(1)
    for fator2 in range(1, 11):
        produto = fator1 * fator2
        print('--> {} X {} = {}'.format(fator1, fator2, produto))
        sleep(0.3)
elif fator1 < 0:
    print('Ok! Tabuada do {}, sem problemas.'.format(fator1))
    sleep(0.5)
    print('PROCESSANDO . . .')
    sleep(1)
    for fator2 in range(1, 11):
        produto = fator1 * fator2
        print('--> {} X {} = {}'.format(fator1, fator2, produto))
        sleep(0.3)
else:
    print('Todo número multiplicado por {}\né igual a zero.\nDigite outro número inteiro.'.format(fator1))
print('{:*^35}'.format(''))
