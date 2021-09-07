#Crie um algoritmo que leia um número e mostre seu dobro,
# triplo e raiz quadrada.
n = eval(input('Digite um número: '))
print('Analisando o número digitado:\nSeu dobro é {}\nSeu triplo é {}\nSua raiz quadrada é {:.2f}'.format(n*2, n*3, n**(1/2)))
