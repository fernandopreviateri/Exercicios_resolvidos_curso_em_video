'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.'''
dados = {}
print('<<>>' * 10)
print(f'{" JOGUELO ":^40}')
print('<<>>' * 10)
dados['nome'] = str(input('Digite o nome do jogador: ').strip().title())
partidas = int(input(f"Quantas partidas {dados['nome'][:]} jogou? "))
dados['partidas'] = partidas
cont_partida = 1
totgols = 0
gols = []
print('Quantos gol(s) foram feitos na:')
for i in range(0, partidas):
	gols.append(int(input(f'{cont_partida}ª partida: ')))
	cont_partida += 1
totgols = sum(gols)
aproveitamento = totgols / partidas
dados['gols'] = gols
dados['totgols'] = totgols
dados['aproveitamento'] = aproveitamento
print('<<>>' * 10)
print(dados)
print('<<>>' * 10)
for i, v in dados.items():
	print(f'O campo {i} tem valor {v}')
print(f'O aproveitamento do jogador {dados["nome"]} foi de {dados["aproveitamento"]:.1f} gol(s) por jogo.')
print('<<>>' * 10)
print(f'{dados["nome"]} jogou {dados["partidas"]} partidas e fez no total de {dados["totgols"]} gol(s).')
cont = 0
for i in range(dados['partidas']):
	print(f'=> Na {i+1}ª partida fez {dados["gols"][cont]} gol(s).')
	cont += 1
print('<<>>' * 10)
