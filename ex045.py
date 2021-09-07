'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
print('{:*^30}'.format(' JOKENPÔ '))
p2 = 0
p1 =int(input('''Escolha:
1 --> Pedra
2 --> Papel
3 --> Tesoura
************* --> '''))
if 0 < p1 <= 3:
    p2 = randint(1, 3)
    print('{}'.format('JO'))
    sleep(0.5)
    print('{}'.format(' KEN'))
    sleep(0.5)
    print('{}'.format('   PÔ'))
    sleep(0.5)
    if p1 == p2:
        print('EMPATE')
    elif p1 == 1 and p2 == 3:
        print('PEDRA QUEBRA A TESOURA.\nVOCÊ GANHOU!')
    elif p1 == 2 and p2 == 1:
        print('PAPEL EMBRULHA A PEDRA.\nVOCÊ GANHOU!')
    elif p1 == 3 and p2 == 2:
        print('TESOURA CORTA O PAPEL.\nVOCÊ GANHOU!')
    elif p2 == 1 and p1 == 3:
        print('PEDRA QUEBRA A TESOURA.\nVOCÊ PERDEU!')
    elif p2 == 2 and p1 == 1:
        print('PAPEL EMBRULHA A PEDRA.\nVOCÊ PERDEU!')
    elif p2 == 3 and p1 == 2:
        print('TESOURA CORTA O PAPEL.\nVOCÊ PERDEU!')
else:
    print('OPÇÃO INVÁLIDA\nTENTE NOVAMENTE')
print('{:^30}'.format('*' * 30))


