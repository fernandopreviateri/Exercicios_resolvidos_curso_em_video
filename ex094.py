'''Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média'''
from time import sleep
media = cont = 0
opcao = str
dados = {}
list = []
print('+=' * 25)
print(f'{"CADASTRELO":^45}\nSeja bem-vindo(a)')
sleep(1)
while True:
    print(f'{" MENU ":-^50}')
    print(f'{"OPÇÃO A: Novo Cadastro"}\n{"OPÇÃO B: Total de pessoas cadastradas"}\n{"OPÇÃO C: Média de idade das pessoas cadastradas"}\n{"OPÇÃO D: Lista todas as mulheres cadastradas"}\n{"OPÇÃO E: Lista pessoas com idade acima da média"}\n{"OPÇÃO F: Sair do programa"}\n{"-" * 50}')
    while True:
        opcao = str(input(f'{"Escolha a opção: "}')).upper().strip()[0]
        if opcao in 'ABCDEF':
            break
        print(f'{"Por favor, digite a letra correspondente."}')
        sleep(0.5)
    if opcao == 'A':
        while True:
            print(f'{"Digite todas as informações:"}')
            dados['nome'] = str(input('Nome: ')).strip().title()
            dados['idade'] = int(input('Idade: '))
            while True:
                dados['sexo'] = str(input('Sexo:\n[M] = Masculino\n[F] = Feminino\n[O] = Outro\n--> ')).strip().upper()[
                    0]
                if dados['sexo'] in 'MFO':
                    break
                print('Por favor, digite a letra correspondente.')
                sleep(1)
            list.append(dados.copy())
            dados.clear()
            print(f'{"SALVANDO DADOS . . ."}')
            sleep(1.5)
            while True:
                novo = str(input('Deseja criar novo cadastro [S/N]? ')).upper().strip()[0]
                if novo in 'SN':
                    break
                print('Por favor, digite a letra correspondente.')
            if novo in 'N':
                break
        continue
    if opcao == 'B':
        if len(list) == 0:
            print(f'{" NÃO FORAM ENCONTRADOS REGISTROS ":*^50}')
            sleep(1)
            continue
        print(f'{" TOTALIZANDO ":.^25}\n{"NOME":<12}{"IDADE":>2}{"SEXO":>8}\n{"_" * 25}')
        for i in range(len(list)):
            print(f'{list[i]["nome"]:<12}{list[i]["idade"]:>5}{list[i]["sexo"]:>8}')
        print(f'{"_" * 25}\n{"TOTAL DE CADASTROS"} {len(list):>6}\n{"." * 25}')
        continue
    if opcao == 'C':
        if len(list) == 0:
            print(f'{" NÃO FORAM ENCONTRADOS REGISTROS ":*^50}')
            continue
        media = 0
        print(f'{" CALCULANDO A MÉDIA ":.^25}')
        for i in range(len(list)):
            media += list[i]["idade"]
        media = (media / len(list))
        print(f'Média idade {media:.2f} ano(s).\n{"." * 25}')
        continue
    if opcao == 'D':
        if len(list) == 0:
            print(f'{" NÃO FORAM ENCONTRADOS REGISTROS ":*^50}')
            continue
        print(f'{" LISTANDO MULHERES ":.^25}\n{"NOME":<12}{"SEXO":>13}\n{"-" * 25}')
        for i in list:
            if i['sexo'] in 'F':
                print(f'{i["nome"]:<12}{i["sexo"]:>13}')
                continue
            elif i['sexo'] in 'M':
                pass
            elif i['sexo'] in 'O':
                pass
        print(f'{"." * 25}')
        continue
    if opcao == 'E':
        media = 0
        if len(list) == 0:
            print(f'{" NÃO FORAM ENCONTRADOS REGISTROS ":*^50}')
            continue
        for i in range(len(list)):
            media += list[i]["idade"]
        media = (media / len(list))
        print(f'{" LISTANDO ACIMA DA MÉDIA ":.^25}\n{"NOME":<12}{"IDADE":>13}\n{"-" * 25}')
        for i in list:
            if i['idade'] > media:
                print(f'{i["nome"]:<12}{i["idade"]:>13}')
        print(f'{"." * 25}\n{"Média idade"} {media:.2f} {"ano(s)."}\n{"." * 25}')
        continue
    if opcao == 'F':
        continuar = str(input('Deseja realmente sair do programa [S/N]? ')).upper().strip()[0]
        while continuar not in 'SN':
            continuar = str(input('Por favor, digite a opção correta.\nDeseja realmente sair do programa [S/N]? ')).upper().strip()[0]
        if continuar == 'S':
            break
    else:
        break
print(f'{"<<>>" * 12}\n{"FIM DO PROGRAMA":^50}\n{"<<>>" * 12}')






