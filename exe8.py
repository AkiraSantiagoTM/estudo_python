nome = input('Digite seu nome: ')

if nome:

    if " " not in nome:
        print(f'O nome {nome} tem {len(nome)} caracteres')
        print(f'A primeira letra é {nome[0]} e a ultima é {nome[-1]}')
        print(f'E o seu nome invertido é: {nome[::-1]} \n')

    else:
        print('Campo nome não pode conter espaço \n')

else:
    print('Campo nome é obrigatório! \n')

# ================================================================================ #

idade = input('Digite sua idade: ')

if idade:

    try:
        idade_int = int(idade)

        if idade_int >= 18:
            print('Voce é maior de idade \n')

        else:
            print('Voce é menor de idade \n')

    except:
        print('Campo idade precisa ser um numero inteiro \n')

else:
    print('Campo idade obrigatório! \n')
    
# ================================================================================ #

usuario = input('Digite seu nome de usuario: ')

if usuario:
    if " " not in usuario:
        if len(usuario) >= 5 and len(usuario) <= 10:

            senha = input('Usúario encontrado, digite sua senha: ')

            if usuario and senha:
                if " " not in senha:
                    if len(senha) >= 6:
                        if senha == usuario:
                            if nome and idade_int and usuario and senha:
                                print('Cadastro concluido')

                        else:
                            print('Senha não pode ser igual ao usuario')

                    else:
                        print('Senha precisa ter no minimo 6 caracteres')

                else:
                    print('Senha não pode conter espaço')

            else:
                print('Necessario senha para fazer o cadastro')

        else:
            print('Campo usuario precisa ter entre 5 a 10 caracteres')

    else:
        print('Campo usario não pode conter espaço')

else:
    print('Campo usuario obrigatório')