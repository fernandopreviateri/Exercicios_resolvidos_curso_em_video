'''Crie um programa que leia a idade e o sexo de várias pessoas. A
cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;
c) Quantas mulheres tem menos de 20 anos.'''
print('CADASTRO DE PESSOAS')
maior18 = total = totm = man = 0
while True:
	idade = int(input('Digite a idade: '))
	sexo = str(input('Digite [M/F]: ')).strip().upper()[0]
	while sexo not in 'MF':
		print('Opção Inválida!\nDigite corretamente.')
		sexo = str(input('Digite [M/F]: ')).strip().upper()[0]
	total += 1
	if idade < 20 and sexo == 'F':
		totm += 1
	if sexo == 'M':
		man += 1
	if idade >= 18:
		maior18 += 1
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
	if resp == 'N':
		break
print(f'Você cadastrou {total} pessoa(s).\n--> {maior18} é/são maior(es) de 18 anos.\n--> {man} é/são homens.\n--> {totm} é/são mulheres menores de 20 anos.')
