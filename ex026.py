'''Faça um mprograma que leia uma frase pelo teclado e mostre:
-> Quantas vezes aparece a letra A;
-> Em que posição ela aparece a primeira vez;
-> Em que posição ela aparece a última vez.'''
frase = str(input('Digite uma frase com efeito de motivação: ')).strip().upper()
print('1º - A letra A aparece {} vez(es).'.format(frase.count('A')))
print('2º - A primeira letra A aparece no {}º caractere.'.format(frase.find('A')+1))
print('3º - A última letra A aparece no {}º caractere.'.format(frase.rfind('A')+1))
