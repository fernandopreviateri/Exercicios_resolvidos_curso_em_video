'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5:
  ABAIXO DO PESO
- Entre 18.5 e 25:
  PESO IDEAL
- Entre 25 até 30:
  SOBREPESO
- 30 até 40:
  OBESIDADE
- Acima de 40:
  Obesidade Mórbida'''
peso = eval(input('Digite seu peso (Kg):\n--> '))
altura = eval(input('Digite sua altura (M):\n--> '))
if peso != 0:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print('Você está ABAIXO DO PESO\nSeu IMC é {:.1f}'.format(imc))
    elif imc < 25:
        print('Você está no PESO IDEAL\nSeu IMC é {:.1f}'.format(imc))
    elif imc < 30:
        print('Você está com SOBREPESO\nSeu IMC é {:.1f}'.format(imc))
    elif imc < 40:
        print('Você está com OBESIDADE\nSeu IMC é {:.1f}'.format(imc))
    elif imc >= 40:
        print('Você está com OBESIDADE MÓRBIDA\nSeu IMC é {:.1f}'.format(imc))
else:
    print('Peso e/ou altura inválida!\nTENTE NOVAMENTE.')
