'''Melhore o jogo do DESAFIO 28 onde o computador vai pensar em
um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer.'''
from random import randint
cont = 1
cpu = randint(0, 10)
name = str(input('Qual é seu nome:\n--> ')).strip().title()
you = int(input('Olá, {}!\nQual o número que pensei?\nDica: de 0 a 10\n--> '.format(name)))
while you != cpu:
    while you > 10 or you < 0:
        you = int(input('{}, você presou atenção na dica?\nVamos lá, digite novamente:\n--> '.format(name)))
        cont +=1
    if you < cpu:
        print('Um pouco mais!')
    else:
        print('Um pouco menos!')
    you = int(input('{} não foi dessa vez!\nTente novamente:\n--> '.format(name)))
    cont +=1
print('{:*^30}\nVocê acertou.\nFoi preciso {} tentativa(s).'.format(' PARABÉNS ', cont))


