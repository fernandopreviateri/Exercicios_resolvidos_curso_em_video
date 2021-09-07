#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a paga, sabendo que
#carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
print('PROGRAMA DE ESTIMATIVA DE CUSTO - ALUGUEL DE CARROS')
dias = eval(input('Digite a quantidade de dias que pretende alugar o carro: '))
km = eval(input('Digite a quantidade de Km que pretende rodar com o carro: '))
print('O valor pelos dias é de R$ {:.2f}\nO valor pelos Km é de R$ {:.2f}\nO total é de R$ {:.2f}'.format(dias*60, km*0.15, ((dias*60)+(km*0.15))))
