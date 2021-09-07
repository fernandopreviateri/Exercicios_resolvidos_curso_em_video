'''Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0:
  REPROVADO
- Média entre 5.0 e 6.9:
  RECUPERAÇÃO
- Média 7.0 ou superior:
  APROVADO'''
print('*' * 15, 'M É D I A  C A L C U L A T I O N', '*' * 15)
nome = str(input('Digite o nome do aluno:\n--> ')).title()
print('Vamos calcular a média do(a) aluno(a) {}.'.format(nome))
nota1 = eval(input('Digite a 1ª nota:\n--> '))
nota2 = eval(input('Digite a 2ª nota:\n--> '))
media = (nota1 + nota2) / 2
if media > 10:
    print('As notas devem ser de 0 a 10.\nTENTE NOVAMENTE.')
elif media < 5:
    print('O aluno(a) {} foi REPROVADO.\nSua média é {:.1f}'.format(nome, media))
elif media >= 5 and media <= 6.99999:
    print('O aluno(a) {} está de RECUPERAÇÃO.\nSua média é {:.1f}'.format(nome, media))
else:
    print('O aluno(a) {} foi APROVADO.\nSua média é {:.1f}'.format(nome, media))
print('*' * 64)
