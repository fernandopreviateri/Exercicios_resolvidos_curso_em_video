'''Faça uma função chamada maior(), que receba vários prâmetros com valores inteiros.
Seu programa terá que analisar todos os valores e dizer qual é o maior.'''
from time import sleep
def maior(* num):
    cont = maior = 0
    print(f'{"Analisando valores . . ."}')
    sleep(1)
    for v in num:
        sleep(0.5)
        print(f'{v} ', end= " ")
        if maior < v:
            maior = v
    print("")
    print(f'{"O maior número é o nº"} {maior}.\n{"+-" * 20}')


# Programa principal
maior(6, 3, 1, 9, 1, 300, 200, 10, 1, 2, 3, 5, 6, 7, 8, 9, 10)
maior(1, 2)
maior(6)
maior()
