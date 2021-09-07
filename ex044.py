'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista em dinheiro/cheque: 10% de desconto;
- à vista no cartão: 5% de desconto;
- em até 2x no cartão: Preço normal;
- em 3x ou mais no cartão: 20% de juros '''
preco = eval(input('Digite o valor da compra:\n--> R$ '))
print('''Escolha a forma de pagamento:
Opção 1: à vista no dinheiro;
Opção 2: à vista no cartão;
Opção 3: 2 x no cartão;
Opção 4: 3 x ou mais no cartão.''')
opcao = int(input('--> '))
if 0 < opcao < 5:
   if opcao == 1:
       total = (preco - (preco * (10 / 100)))
       print('O valor da sua compra com desconto é R$ {:.2f}'.format(total))
   elif opcao == 2:
       total = (preco - (preco * (5 / 100)))
       print('O valor da sua compra com desconto é R$ {:.2f}'.format(total))
   elif opcao == 3:
       total = preco
       print('O valor da sua compra é R$ {:.2f}\n2 X R$ {:.2f}'.format(total, (total / 2)))
   elif opcao == 4:
       qtd_parc = int(input('Digite a quantidade de parcelas:\n--> '))
       total = (preco + (preco * (20 / 100)))
       print ('O valor total da sua compra é R$ {:.2f} com juros.\n{} x {:.2f}'.format(total, qtd_parc, (total / qtd_parc)))
else:
    print('''Opção inválida!
TENTE NOVAMENTE. ''')
