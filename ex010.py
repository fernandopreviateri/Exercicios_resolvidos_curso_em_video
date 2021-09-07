#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar.
#Considere US$ 1.00 = R$ 3,27
print('Bem-vindo(a) ao CONVERSOR DE MOEDAS\n')
din = eval(input('Quanto de dinheiro você tem na carteira? R$ '))
print('Você pode comprar US$ {:>.2f}'.format((din/5.56)))
print('Você pode comprar EUR {:>.2f}'.format((din/6.47)))
print('Você pode comprar JPY {:>.2f}'.format((din/0.053)))
