'''Faça um programa que leia nome e média de um aluno, guardando em situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
média >= 7 APROVADO
média <  7 REPROVADO'''
cont = 'S'
nome = str
nota1 = nota2 = 0
dados = {}
alunos = []
print('-' * 30)
print('{:.^30}'.format(' ESCOLARE '))
while cont in 'S':
	print('Digite todas as informações:')
	dados['nome'] = str(input('Nome do(a) aluno(a): ').lower().title())
	dados['nota1'] = eval(input('1ª nota: ')) * 0.40
	dados['nota2'] = eval(input('2ª nota: ')) * 0.60
	dados['media'] = (dados['nota1'] + dados['nota2'])
	if dados['media'] >= 7:
		dados['situacao'] = 'APROVADO'
	elif 5 <= dados['media'] < 7:
		dados['situacao'] = 'RECUPERAÇÃO'
	else:
		dados['situacao'] = 'REPROVADO'
	print('Dados salvos com sucesso!')
	print('{:.^30}'.format(''))
	alunos.append(dados.copy())
	cont = str(input('Deseja continuar [S/N]? ').strip().upper()[0])
	while cont not in 'SN':
		cont = str(input('Por favor, digite a opção correta.\nDeseja continuar [S/N]? ').strip().upper()[0])
print('{:.^30}'.format(' BOLETIM '))
for i in range(len(alunos)):
	print(f'{alunos[i]["nome"]:<12}{alunos[i]["media"]:>4.1f}{alunos[i]["situacao"]:>14}')
print('{:.^30}'.format(''))

