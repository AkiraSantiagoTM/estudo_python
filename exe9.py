nome = input('Digite seu nome: ')
print('================================================')

if nome:
    if " " not in nome:
        if len(nome) >= 3:

            print(
            f'Nome: {nome} \n'
            f'Quantidade de caracteres: {len(nome)} \n'
            f'Primeira letra: {nome[0]} \n'
            f'Última letra: {nome[-1]} \n'
            f'Nome invertido: {nome[::-1]}\n'
            f'================================================'
            )

            idade = input("Digite sua idade: ")

        else:
            print('Campo nome precisa conter no minimo 3 caracteres!')
    else:
        print('Campo nome não pode conter espaço!')
else:
    print('Campo nome obrigatório!')

# ========================================================================================================== #

try:
    if idade:
        try:
            idade_int = int(idade)
            print('================================================')

            filme = input('Escolha o filme: ')
                
        except ValueError:
            print('Idade precisa ser um número inteiro')
    else:
        print('Campo idade obrigatório!')
except:
    print('Feche o programa e tente novamente')

# ========================================================================================================== #

try:
    if filme:
        if filme == 'aventura' or filme == 'terror' or filme == 'animacao':

            if filme == 'aventura' and idade_int >= 12 or filme == 'terror' and idade_int >= 18 or filme == 'animacao':
                sessao = input('Escolha a sessão: ')
            else:
                print("Você não possui idade suficiente para assistir esse filme.")

        else:
            print('Filme não encontrado')
    else:
        print('Campo filme obrigatório!')
except:
    print('Feche o programa e tente novamente')

# ========================================================================================================== #

try:
    if sessao:
        if sessao == 'manha' or sessao == 'tarde' or sessao == 'noite':
            print('================================================')
            cupom = input('Deseja incluir um cupom de desconto? ')
                
        else:
            print('Sessão inválida!')
    else:
        print('Campo sessão obrigatório!')
except:
    print('Feche o programa e tente novamente')

# ========================================================================================================== #

try:
    if cupom:
        if cupom == "sim" or cupom == "Sim":
            cupom_inserido = input('Digite o cupom: ')

            if cupom_inserido == "PYTHON10":
                print('Cupom aplicado! \n'
                    '================================================ \n'
                    'INGRESSO CONFIRMADO \n\n'
                    f'Nome: {nome} \n'
                    f'Filme: {filme} \n'
                    f'Sessão: {sessao} \n'
                    f'Idade: {idade_int} \n\n'
                    'Cupom aplicado! \n'
                    'COMPRA REALIZADA COM SUCESSO! \n'
                    )
            else:
                print('Cupom inválido!')

        else:
            print('Usuario não quer utilizar cupom! \n'
                '================================================ \n'
                'INGRESSO CONFIRMADO \n\n'
                f'Nome: {nome} \n'
                f'Filme: {filme} \n'
                f'Sessão: {sessao} \n'
                f'Idade: {idade_int} \n\n'
                'COMPRA REALIZADA COM SUCESSO! \n'
                )
    else:
        print('Nenhum cupom aplicado! \n'
            '================================================ \n'
            'INGRESSO CONFIRMADO \n\n'
            f'Nome: {nome} \n'
            f'Filme: {filme} \n'
            f'Sessão: {sessao} \n'
            f'Idade: {idade_int} \n\n'
            'COMPRA REALIZADA COM SUCESSO! \n'
            )
except:
    print('Feche o programa e tente novamente')