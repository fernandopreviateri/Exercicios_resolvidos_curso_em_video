'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais o aumento é de 15%.'''

print('-=' * 10, 'C A L C U L A  A U M E N T O', '-=' * 10)
salario = eval(input('Digite o valor do salário para receber o aumento R$: '))
if salario > 1250.00:
    aumento10 = ((salario * (10/100)))
    print('O aumento é de R$ {:.2f}\nAssim, o novo salário é de R$ {:.2f}'.format(aumento10, salario + aumento10))
else:
    salario <= 1250.00
    aumento15 = ((salario * (15/100)))
    print('O aumento é de R$ {:.2f}\nAssim, o novo salário é de R$ {:.2f}'.format(aumento15, salario + aumento15))
