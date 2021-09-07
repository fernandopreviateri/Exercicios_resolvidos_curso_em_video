'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular(largura e comprimento) e mostre a área do terreno. '''

def area():
    print('*' * 40)
    print(f'{"ÁREA CALCULATION":^40}')
    l = float(input("Digite a largura do terreno metros: ").strip())
    c = float(input("Digite o comprimento do terrero em metros: ").strip())
    m2 = (l * c)
    print('*' * 40)
    print(f'A área de um terro com {l}m de largura e\n{c}m de comprimento é igual {m2:.2f}m².')
    print('*' * 40)


#Programa principal
area()
