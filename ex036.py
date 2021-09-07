'''Escreva um programa para aprovar um empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado.'''
from time import sleep
print('-=' * 10, ' H A B I T A C R E D', '=-' * 10)
valor_financiado = eval(input('Digite o valor da casa em R$ '))
renda = eval(input('Digite o valor da renda em R$ '))
prazo = eval(input('Quantos anos precisa para pagar? '))
print('ANALISANDO')
sleep(3)
qtd_parcela = prazo * 12
v_parcela = valor_financiado / qtd_parcela
if v_parcela > (renda * (30/100)):
    print('Sentimos muito, mas seu empréstimo\nNÃO foi aprovado.\nA parcela de R$ {:.2f} excede seu limite máximo.'.format(v_parcela))
else:
    print('PARABÉNS!\nSeu empréstimo foi aprovado.\nValor financiado: R$ {:.2f}\nNúmero de parcelas: {}\nValor de cada parcela R$ {:.2f}.'.format(valor_financiado, qtd_parcela, v_parcela))
print('-=' * 31)
