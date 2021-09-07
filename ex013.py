#Faça um algoritmo que leia o salário de um funcionário e mostre
#seu novo salário, com 15% de aumento.
print('Bem-vindo(a) ao PAAS - Programa de Análise de Aumento de Salário')
nome_fun = str(input('Digite o nome do funcionário: '))
salario_atual = eval(input('Digite o salário atual de {} R$ '.format(nome_fun)))
print('O funcionário(a) {} está autorizado(a)\na receber um aumento de salário por cumprir as metas.\nSeu salário atual é de R$ {}'.format(nome_fun, salario_atual))
percentual = eval(input('Digite o percentual de aumento: '))
print('{} teve um acréscimo de R$ {:.2F} no seu salário.\nPortanto, seu novo salário é de R$ {:.2f} .'.format(nome_fun, ((percentual/100)*salario_atual), (salario_atual+((percentual/100)*salario_atual))))

