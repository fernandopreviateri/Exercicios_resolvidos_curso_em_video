'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável
Ex: escreva('Olá Mundo')
Saída:
Saída:
-----------
Olá, Mundo!
-----------'''


def escreva():
    for i in range(1, 4):
        frase = str(input(f'Digite a {i}ª frase: ')).strip()
        mult = len(frase) + 4
        print(f'{"~" * mult}\n{frase}\n{"~" * mult}')


# Programa principal
escreva()
