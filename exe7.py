nome = input('Digite seu nome: ')

if nome:

    if " " not in nome:
        qtd_nome = len(nome)
        primeira_letra = nome[0]
        ultima_letra = nome[-1]
        invertido = nome[::-1]

        print(' ')

        if qtd_nome >= 1 and qtd_nome <= 4:
            print(f'O {nome} é curto')

        elif qtd_nome >= 5 and qtd_nome <= 6:
            print(f'O {nome} é  normal')

        else:
            print(f'O {nome} é longo')

        print(f'Quantidade de caracteres: {qtd_nome} \n'
              f'A primeira letra do nome é: {primeira_letra} \n'
              f'A ultima letra do nome é: {ultima_letra} \n'
              f'E o nome invertido: {invertido} \n'
              )

    else:
        print('Nome não pode ter espaço!')

    cargo = input('Digite seu cargo: ')
    cargos_autorizados = "admin, gerente, supervisor"

    if cargo in cargos_autorizados:

        print(f'Seu cargo: {cargo}')
        senha = input('Está autorizado, digite sua senha para acessar: ')

        if senha:

            if len(senha) <= 6:

                if " " not in senha:
                    print('Senha aceita')

                else:
                    print('Senha não pode conter espaço')

            else:
                print('Senha precisa ter no maximo 6 caracteres')

        else:
            print('Senha obrigatória!')

    else:
        print(f'Seu cargo: {cargo}')
        print('Não esta autorizado \n')

else:
    print('Campo nome obrigatório!')