'''Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores M ou F. Caso esteja errado, peça a digitação novamente
até ter um valor correto'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Por favor, digite corretamente:\n- Para masculino, digite M:\n- Para feminino,  digite F:\n--> ')).upper().strip()
if sexo == 'M':
    sexo = 'MASCULINO'
    print('{}Sexo digitado corretamente. {}'.format('*** ', '***'))
    print(sexo)
elif sexo == 'F':
    sexo = 'FEMININO'
    print('{}Sexo digitado corretamente. {}'.format('*** ', '***'))
    print(sexo)




