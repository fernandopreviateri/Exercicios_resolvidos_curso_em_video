'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = eval(input('Digite o 1º número:\n--> '))
n2 = eval(input('Digite o 2º número:\n--> '))
opcao = 0
while True:
    while opcao < 5:
        print('{:*^30}'.format(' MENU '))
        opcao = int(input('Digite:\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR\n--> '))
        if opcao == 1:
            resultado = n1 + n2
            print('A soma de {} + {} é = {}\nCARREGANDO . . .'.format(n1, n2, resultado))
        elif opcao == 2:
            resultado = n1 * n2
            print('O produto de {} * {} é = {}\nCARREGANDO. . .'.format(n1, n2, resultado))
        elif opcao == 3:
             if n1 > n2:
                 print('O primeiro número {} é o MAIOR'.format(n1))
             elif n2 > n1:
                 print('O segundo número {} é o MAIOR'.format(n2))
             else:
                 print('Os dois números {} e {} são iguais.\nCARREGANDO . . .'.format(n1, n2))
        elif opcao == 4:
            n1 = eval(input('Digite o 1º número\n--> '))
            n2 = eval(input('Digite o 2º número\n--> '))
            opcao = 0
        sleep(0.3)
    e = str(input('Deseja realmente sair?\nS/N--> ')).strip().upper()[0]
    if e == 'S':
        break
    opcao = 0
    sleep(0.3)
print('PROGRAMA ENCERRADO')
