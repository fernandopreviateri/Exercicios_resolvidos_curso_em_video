'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor de 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando a flag).'''
n = soma = cont = 0
while True:
	n = int(input('Digite um número ou 999 p/ sair\n--> '))
	if n == 999:
		break
	soma += n
	cont += 1
print(f'Você digitou {cont} vez(es).\nA soma dos números digitados é igual a {soma} .')
