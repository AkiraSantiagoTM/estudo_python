nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

if nome and sobrenome:
    print(F"Seu nome completo é: {nome} {sobrenome}")

    if idade:
        idade_int = int(idade)

        if idade_int >= 18:
            print(f'Nasceu em {2026 - idade_int} e é maior de idade! ')

            if altura:
                altura_float = float(altura)

                if altura_float >= 1.70:
                    print(f'Voce tem {altura_float:.2f}m e é acima da média')

                else:
                    print(f'Voce tem {altura_float:.2f}m e é abaixo da média')


            else:
                print('Campo altura é obrigatório')

        else:
            print('Voce é menor de idade!')
        

    else:
        print('Campo idade orbigatório!')


else:
    print('Campo nome e sobrenome obrigatórios!')