'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
dados_futebol = {}
dados_volei = {}
dados_basquete = {}
list_futebol = []
list_volei = []
list_basquete = []
partida = []
confirmar = str
print('*' * 40)
print(f'{"GERENCIA PLAYER":^40}\n{"*" * 40}\n{"Seja bem-vindo(a)."}')
while True:
	print(f'{"<<>>" * 10}\n{"MENU DESPORTE":-^40}')
	print(f'{"OPÇÃO 1 - Futebol"}\n{"OPÇÃO 2 - Volei"}\n{"OPÇÃO 3 - Basquete"}\n{"OPÇÃO 4 - Fechar Programa"}\n{"-" * 40}')
	while True:
		opcao_desporte = str(input('Digite a opção desejada: ').strip())
		if opcao_desporte in '1234':
			break
		print(f'{"Por favor, digite a opção correspondente."}')
	while True:
		if opcao_desporte == '1':
			print(f'{"<<>>" * 10}\n{"MENU FUTEBOL":-^40}')
			print(f'{"- OPÇÃO 1: Cadastrar Jogador"}\n{"- OPÇÃO 2: Análise Detalhada de Jogador"}\n{"- OPÇÃO 3: Relatório"}\n{"- OPÇÃO 4: Voltar"}\n{"":-^40}')
			while True:
				opcao_futebol = str(input('Digite o número da opção desejada: ').strip())
				if opcao_futebol in '1234':
					break
				print(f'{"Por favor, digite o número da opção correspondente"}')
			if opcao_futebol == '1':
				while True:
					print(f'{"Digite todas as infomações solicitadas:"}')
					dados_futebol['nome'] = str(input('Nome do jogador: ')).strip().title()
					dados_futebol['idade'] = int(input('Idade: '))
					dados_futebol['camisa'] = int(input('Veste a camisa nº '))
					dados_futebol['jogos'] = int(input('Quantos jogos o jogador participou: '))
					jogos = dados_futebol['jogos']
					if jogos > 0:
						for i in range(1, jogos+1):
							partida.append(int(input(f'{"Quantos gols foram feitos na"} {i}{"ª partida:"} ')))
						dados_futebol['gols'] = partida.copy()
						dados_futebol['media'] = round((sum(partida) / jogos), 1)
					else:
						print(f'{" DESCULPE! ":*^40}\n{"O cadastro é feito para jogador titular."}')
						break
					list_futebol.append(dados_futebol.copy())
					partida.clear()
					del jogos
					dados_futebol.clear()
					print(list_futebol)
					while True:
						novo = str(input('Deseja cadastrar novo jogador [S/N]? ')).strip().upper()[0]
						if novo in 'SN':
							break
						print(f'{"Por favor, digite a opção correta."}')
					if novo == 'S':
						continue
					break
				continue

			if opcao_futebol == '2':
				while True:
					if len(list_futebol) == 0:
						print(f'{"*" * 40}\n{" NÃO HÁ JOGADOR CADASTRADO ":*^40}\n{"*" * 40}')
						continue
					print(f'{"-" * 40}\n{"Escolha a ID correspondente ao jogador"}\n{"ID":<4}{"NOME":<12}')
					i = 0
					for i, a in enumerate(list_futebol):
						print(f'{i:<4}{list_futebol[i]["nome"]}')
					print("-" * 40)
					while True:
						relatorio = int(input(f'Digite a ID referente ao nome do jogador.\nPara sair digite 99999: '))
						if relatorio == 99999:
							break
						elif relatorio > len(list_futebol):
							print(f'{"Índice Inválido!"}')
							continue
						else:
							print(f'{" RELATÓRIO GERENCIAL ":*^40}')
							print(f'Jogador: {list_futebol[relatorio]["nome"]}\nIdade: {list_futebol[relatorio]["idade"]} anos\nVeste a camisa: {list_futebol[relatorio]["camisa"]}\nParticipação de jogos: {list_futebol[relatorio]["jogos"]}\nTotal de Gols: {sum(list_futebol[relatorio]["gols"])}')
							cont = 1
							if list_futebol[relatorio]["media"] > 1:
								print(f'Média de gols por partida: {list_futebol[relatorio]["media"]}')
								for i in list_futebol[relatorio]["gols"]:
									print(f'{cont}ª partida marcou {i} gols.')
									cont += 1
							print('*' * 40)
					break
				continue
			if opcao_futebol == '3':
				if len(list_futebol) == 0:
					print(f'{"*" * 40}\n{" NÃO HÁ JOGADOR CADASTRADO ":*^40}\n{"*" * 40}')
					continue
				print(f'{"*" * 40}\n{"JOGADORES":^40}\n{"-" * 40}\n{"Nome":<15}{"Idade":<7}{"Camisa":<8}{"Total Gols":>4}')
				for i in range(len(list_futebol)):
					print(f'{list_futebol[i]["nome"]:<15}{list_futebol[i]["idade"]:>5}{list_futebol[i]["camisa"]:>8}{sum(list_futebol[i]["gols"]):>12}')
				print(f'{"-" * 40}')
			if opcao_futebol == '4':
				break
		if opcao_desporte == '2':
			print(f'{"<<>>" * 10}\n{"MENU VOLEI":-^40}')
			print(f'{"- OPÇÃO 1: Cadastrar Jogador"}\n{"- OPÇÃO 2: Análise Detalhada de Jogador"}\n{"- OPÇÃO 3: Relatório"}\n{"- OPÇÃO 4: Voltar"}\n{"":-^40}')
			while True:
				opcao_volei = str(input('Digite o número da opção desejada: ').strip())
				if opcao_volei in '1234':
					break
				print(f'{"Por favor, digite o número da opção correspondente"}')
			if opcao_volei == '1':
				while True:
					print(f'{"Digite todas as infomações solicitadas:"}')
					dados_volei['nome'] = str(input('Nome do jogador: ')).strip().title()
					dados_volei['idade'] = int(input('Idade: '))
					dados_volei['camisa'] = int(input('Veste a camisa nº '))
					dados_volei['jogos'] = int(input('Quantos jogos o jogador participou: '))
					jogos = dados_volei['jogos']
					if jogos > 0:
						for i in range(1, jogos+1):
							partida.append(int(input(f'{"Quantos pontos foram feitos na"} {i}{"ª partida:"} ')))
						dados_volei['pontos'] = partida.copy()
						dados_volei['media'] = round((sum(partida) / jogos), 1)
					else:
						print(f'{" DESCULPE! ":*^40}\n{"O cadastro é feito para jogador titular."}')
						break
					list_volei.append(dados_volei.copy())
					partida.clear()
					del jogos
					dados_volei.clear()
					print(list_volei)
					while True:
						novo = str(input('Deseja cadastrar novo jogador [S/N]? ')).strip().upper()[0]
						if novo in 'SN':
							break
						print(f'{"Por favor, digite a opção correta."}')
					if novo == 'S':
						continue
					break
			if opcao_volei == '2':
				if len(list_volei) == 0:
					print(f'{"*" * 40}\n{" NÃO HÁ JOGADOR CADASTRADO ":*^40}\n{"*" * 40}')
					continue
				print(f'{"-" * 40}\n{"Escolha a ID correspondente ao jogador"}\n{"ID":<4}{"NOME":<12}')
				i = 0
				for i, a in enumerate(list_volei):
					print(f'{i:<4}{list_volei[i]["nome"]}')
				print("-" * 40)
				while True:
					relatorio = int(input(f'Digite a ID referente ao nome do jogador\npara sair digite 99999: '))
					if relatorio == 99999:
						break
					print(f'{" RELATÓRIO GERENCIAL ":*^40}')
					print(f'Jogador: {list_volei[relatorio]["nome"]}\nIdade: {list_volei[relatorio]["idade"]} anos\nVeste a camisa: {list_volei[relatorio]["camisa"]}\nParticipação de jogos: {list_volei[relatorio]["jogos"]}\nTotal de Pontos: {sum(list_volei[relatorio]["pontos"])}')
					cont = 1
					if list_volei[relatorio]["media"] > 1:
						print(f'Média de pontos por partida: {list_volei[relatorio]["media"]}')
						for i in list_volei[relatorio]["pontos"]:
							print(f'{cont}ª partida marcou {i} pontos.')
							cont += 1
					print('*' * 40)
					break
			if opcao_volei == '3':
				if len(list_volei) == 0:
					print(f'{"*" * 40}\n{" NÃO HÁ JOGADOR CADASTRADO ":*^40}\n{"*" * 40}')
					continue
				print(f'{"*" * 40}\n{"JOGADORES":^40}\n{"-" * 40}\n{"Nome":<13}{"Idade":<7}{"Camisa":<8}{"Total Pontos":>6}')
				for i in range(len(list_volei)):
					print(f'{list_volei[i]["nome"]:<15}{list_volei[i]["idade"]:>3}{list_volei[i]["camisa"]:>8}{sum(list_volei[i]["pontos"]):>14}')
				print(f'{"-" * 40}')
			if opcao_volei == '4':
				break
		if opcao_desporte == '3':
			print(f'{"<<>>" * 10}\n{"MENU BASQUETE":-^40}')
			print(f'{"- OPÇÃO 1: Cadastrar Jogador"}\n{"- OPÇÃO 2: Análise Detalhada de Jogador"}\n{"- OPÇÃO 3: Relatório"}\n{"- OPÇÃO 4: Voltar"}\n{"":-^40}')
			while True:
				opcao_basquete = str(input('Digite o número da opção desejada: ').strip())
				if opcao_basquete in '1234':
					break
				print(f'{"Por favor, digite o número da opção correspondente"}')
			if opcao_basquete == '1':
				while True:
					print(f'{"Digite todas as infomações solicitadas:"}')
					dados_basquete['nome'] = str(input('Nome do jogador: ')).strip().title()
					dados_basquete['idade'] = int(input('Idade: '))
					dados_basquete['camisa'] = int(input('Veste a camisa nº '))
					dados_basquete['jogos'] = int(input('Quantos jogos o jogador participou: '))
					jogos = dados_basquete['jogos']
					if jogos > 0:
						for i in range(1, jogos+1):
							partida.append(int(input(f'{"Quantos pontos foram feitos na"} {i}{"ª partida:"} ')))
						dados_basquete['pontos'] = partida.copy()
						dados_basquete['media'] = round((sum(partida) / jogos), 1)
					else:
						print(f'{" DESCULPE! ":*^40}\n{"O cadastro é feito para jogador titular."}')
						break
					list_basquete.append(dados_basquete.copy())
					partida.clear()
					del jogos
					dados_basquete.clear()
					print(list_basquete)
					while True:
						novo = str(input('Deseja cadastrar novo jogador [S/N]? ')).strip().upper()[0]
						if novo in 'SN':
							break
						print(f'{"Por favor, digite a opção correta."}')
					if novo == 'S':
						continue
					break
			if opcao_basquete == '2':
				if len(list_basquete) == 0:
					print(f'{"*" * 40}\n{" NÃO HÁ JOGADOR CADASTRADO ":*^40}\n{"*" * 40}')
					continue
				print(f'{"-" * 40}\n{"Escolha a ID correspondente ao jogador"}\n{"ID":<4}{"NOME":<12}')
				i = 0
				for i, a in enumerate(list_basquete):
					print(f'{i:<4}{list_basquete[i]["nome"]}')
				print("-" * 40)
				while True:
					relatorio = int(input(f'Digite a ID referente ao nome do jogador\npara sair digite 99999: '))
					if relatorio == 99999:
						break
					print(f'{" RELATÓRIO GERENCIAL ":*^40}')
					print(f'Jogador: {list_basquete[relatorio]["nome"]}\nIdade: {list_basquete[relatorio]["idade"]} anos\nVeste a camisa: {list_basquete[relatorio]["camisa"]}\nParticipação de jogos: {list_basquete[relatorio]["jogos"]}\nTotal de Pontos: {sum(list_basquete[relatorio]["pontos"])}')
					cont = 1
					if list_basquete[relatorio]["media"] > 1:
						print(f'Média de pontos por partida: {list_basquete[relatorio]["media"]}')
						for i in list_basquete[relatorio]["pontos"]:
							print(f'{cont}ª partida marcou {i} pontos.')
							cont += 1
					print('*' * 40)
					break
			if opcao_basquete == '3':
				if len(list_basquete) == 0:
					print(f'{"*" * 40}\n{" NÃO HÁ JOGADOR CADASTRADO ":*^40}\n{"*" * 40}')
					continue
				print(f'{"*" * 40}\n{"JOGADORES":^40}\n{"-" * 40}\n{"Nome":<13}{"Idade":<7}{"Camisa":<8}{"Total Pontos":>6}')
				for i in range(len(list_basquete)):
					print(f'{list_basquete[i]["nome"]:<15}{list_basquete[i]["idade"]:>3}{list_basquete[i]["camisa"]:>8}{sum(list_basquete[i]["pontos"]):>14}')
				print(f'{"-" * 40}')
			if opcao_basquete == '4':
				break
		if opcao_desporte == '4':
			while True:
				confirmar = str(input('Deseja realmente sair do programa [S/N]? ')).upper().strip()[0]
				if confirmar in 'SN':
					break
				print('Por favor, digite a opção correta.')
			break
		break
	if confirmar == 'S':
		break
print("FIM DO PROGRAMA")
