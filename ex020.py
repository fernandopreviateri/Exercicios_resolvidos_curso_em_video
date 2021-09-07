#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
#trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
#a ordem sorteada.
from random import shuffle
al_1 = str(input('Digite o nome do primeiro aluno: '))
al_2 = str(input('Digite o nome do segundo aluno: '))
al_3 = str(input('Digite o nome do terceiro aluno: '))
al_4 = str(input('Digite o nome do quarto aluno: '))
list = [al_1, al_2, al_3, al_4]
shuffle(list)
print('A ordem para a apresentação dos trabalhos é:\n{}'.format(list))
