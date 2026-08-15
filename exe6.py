"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_digitado = input('Digite seu nome de usúario: ')
qtd_nome = len(nome_digitado)

curto = qtd_nome >= 1 and qtd_nome <= 4
medio = qtd_nome >= 5 and qtd_nome <= 6
longo = qtd_nome >= 7 and qtd_nome <= 12

possui_espaco = " " not in nome_digitado

if nome_digitado and possui_espaco:

    if curto:
        print(f'Seu nome {nome_digitado} possui {qtd_nome} caracteres e é curto')

    elif medio:
        print(f'Seu nome {nome_digitado} possui {qtd_nome} caracteres e é medio')

    elif longo:
        print(f'Seu nome {nome_digitado} possui {qtd_nome} caracteres e é longo')

    else:
        print('Necessario nome de usuario ter entre 1 e 12 caracteres')

else:
    print('Campo nome é obrigatório e não pode possuir espaço!')