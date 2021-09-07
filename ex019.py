#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
al_1 = input('Digite o nome do Aluno: ')
al_2 = input('Digite o nome do Aluno: ')
al_3 = input('Digite o nome do Aluno: ')
al_4 = input('Digite o nome do Aluno: ')
list = [al_1, al_2, al_3, al_4]
print('O aluno escolhido foi: {}'.format(choice(list)))

