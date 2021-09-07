'''Crie uma tupla preenchida com os 20 primeiros colocados da
tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os 4 últimos colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tabela está o time da chapecoense.'''
from time import sleep
times = (('flamengo', 'atlético-MG', 'fluminense', 'são paulo', 'santos', 'palmeiras', 'fortaleza',
		 'grêmio', 'ceará-SC', 'sport', 'recife', 'corinthians', 'bahia', 'bragantino-SP', 'botafogo',
		 'vasco da gama', 'athetico-PR', 'chapecoense', 'goiás', 'oeste'))
confirm = 'S'
while confirm == 'S':
	print('{:*^53}'.format(' TABELA BRASILEIRÃO 2020 '))
	sleep(1)
	print('Opção A: Exibir os cinco primeiros colocados;\nOpção B: Exibir os quatro últimos colocados da tabela;\nOpção C: Exibir todos os times em ordem alfabética;\nOpção D: Exibir que posição está o time Chapecoense.')
	opcao = str(input('{:<}'.format('Escola a opção: '))).strip().upper()
	while opcao not in 'ABCD':
		print('Por favor, digite a opção correta')
		sleep(0.5)
		opcao = str(input('{:<}'.format('Escola a opção: '))).strip().upper()
	if opcao == 'A':
		print('-' * 53)
		print('Os cinco primeiros são:')
		print(f'1ª {times[0]}\n2ª {times[1]}\n3ª {times[2]}\n4ª {times[3]}\n5ª {times[4]}'.title())
	elif opcao == 'B':
		print('-' * 53)
		print('Os quatros últimos são:')
		print(f'17ª {times[-4]}\n18ª {times[-3]}\n19ª {times[-2]}\n20ª {times[-1]}'.title())
	elif opcao == 'C':
		print('-' * 53,'\nTabela de times organizada em ordem alfabética:')
		for cont in range(0, len(times)):
			print(f'{sorted(times)[cont].title()}')
			cont += 1
		print('-' * 53)
	else:
		print('-' * 53)
		print(f'O time da Chapecoense está na {times.index("chapecoense")+1}ª posição.')
	confirm = str(input('Deseja continuar [S/N]?')).strip().upper()
	while confirm not in 'SN':
		print('Por favor, escolha a opção correta.')
		confirm = str(input('Deseja continuar [S/N]? ')).strip().upper()
	if confirm == 'N':
		break
print('{:*^53}'.format(' FIM DO PROGRAMA '))


