#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.
preco = eval(input('Digite o preço do produto R$ '))
print('Pagamento a prazo: R$ {:.2f} com 5% de juros.\nPagamento 30 dias: R$ {:.2f}\nPagamento à vista: R$ {:.2f} com 5% de desconto.'.format(((preco*0.05)+preco), preco, ((preco*0.05)-preco)*-1))
