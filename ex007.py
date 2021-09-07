#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
nome = str(input('Digite o nome do aluno(a); '))
n1 = eval(input('Digite a 1ª nota: '))
n2 = eval(input('Digite a 2ª nota: '))
print('A média do aluno(a),{} é {:.1f}'.format(nome, (n1+n2)/2))
