'''Crie um programa que leia: nome, ano de nascimento e carteira de trabalho
e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de zero
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar. Pra aposentar 35 anos'''
from datetime import datetime
dados = {}
ano = datetime.now().year
print('Digite as informações do trabalhador:')
dados['nome'] = str(input('Nome: ')).strip().title()
dados['ano'] = int(input('Ano de Nascimento: '))
dados['idade'] = ano - dados['ano']
if dados['idade'] < 14:
	print('<<>>' * 10)
	print(f'{dados["nome"]} é menor de idade. Ele tem {dados["idade"]} anos.')
elif 14 <= dados['idade'] <= 16:
	dados['ctps'] = int(input('CTPS Nº: '))
	if dados['ctps'] == 0:
		print('<<>>' * 10)
		print(f'{dados["nome"]} está na faixa de jovem aprendiz,\nsua idade é de {dados["idade"]} anos e não possui CTPS.')
	else:
		print('<<>>' * 10)
		print(f'Trabalhador: {dados["nome"]}\nIdade: {dados["idade"]} anos\nCTPS nº: {dados["ctps"]}\nModalidade: Jovem aprendiz.')
elif dados["idade"] > 16:
	dados['ctps'] = int(input('CTPS Nº: '))
	if dados["ctps"] == 0:
		print('<<>>' * 10)
		print(f'Trabalhador {dados["nome"]}\nIdade: {dados["idade"]} anos.\nNão possui registro e/ou sem CTPS.')
	else:
		dados['anocont'] = int(input('Ano de Contratação: '))
		dados['salario'] = eval(input('Salário R$: '))
		apo = (dados["anocont"] - dados["ano"]) + 35
		print('<<>>' * 10)
		print(f'Trabalhador: {dados["nome"]}\nIdade: {dados["idade"]} anos\nSalário R$ {dados["salario"]:.2f}\nAno de contratação: {dados["anocont"]}\nIrá se aposentar com {apo} anos.')

