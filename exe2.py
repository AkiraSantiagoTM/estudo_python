nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome possui espaço: {" " in nome}')
    print(f'Seu nome possui: {len(nome)} caracteres')
    print(f'A primeira letra de seu nome é: {nome[0]}')
    print(f'A ultima letra de seu nome é: {nome[-1]} \n')

    if idade:
        idade_int = int(idade)
        print(f'Nasceu no ano de: {idade_int - 2026}')

        if idade_int >= 18:
            print('E é maior de idade')

        else:
            print('E é menor de idade')

    else:
        print('Campo idade obrigatório!')

else:
    print('Campo nome obrigatório!')