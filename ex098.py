'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo e realize a contagem.

Seu programa terá que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada. '''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p*= -1
    if p ==0:
        p = 1
    if i < f:
        print(f'Iniciando contagem de {i} até {f} de {p} em {p}.')
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
        print('Fim!')
        print(f'{"+" * 25}')
    else:
        print(f'Iniciando contagem de {i} até {f} de {p} em {p}.')
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= p
        print('FIM!')
        print(f'{"+" * 17}')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)

print(f'Agora é sua vez!')
ini = int(input('Digite o início:   '))
fim = int(input('Digite o fim:      '))
pas = int(input('Digite o passo:    '))
contador(ini, fim, pas)
