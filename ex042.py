'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais;
- Isósceles: Dois lados iguais;
- Escaleno: Todos os lados diferentes'''
seg1 = eval(input('Digite o 1º segmento: '))
seg2 = eval(input('Digite o 2º segmento: '))
seg3 = eval(input('Digite o 3º segmento: '))
if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg2 + seg1):
    print('As retas FORMAM UM TRIÂNGULO ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO.')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('As retas NÃO FORMAM UM TRIÂNGULO.')
