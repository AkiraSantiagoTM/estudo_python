### Calculadora Python ###
while True:
    
    numb_1 = input('Digite um numero: ')
    operador = input('Digite um operador (+-*/): ')
    operador_permitido = '+-*/'
    numb_2 = input('Digite outro numero: ')

    try:
        numb_1_float = float(numb_1)
        numb_2_float = float(numb_2)

    except ValueError:
        print('Um ou ambos os valores são invalidos!')
        continue

    if operador in operador_permitido and len(operador) == 1:
        if operador == "+":
            print(f'{numb_1_float} + {numb_2_float} = {numb_1_float + numb_2_float}')
        elif operador == "-":
            print(f'{numb_1_float} - {numb_2_float} = {numb_1_float - numb_2_float}')
        elif operador == "/":
            if numb_2_float != 0:
                print(f'{numb_1_float} / {numb_2_float} = {numb_1_float / numb_2_float}')
            else:
                print('Não é possivel dividir por 0!')
                continue 
        elif operador == "*":
            print(f'{numb_1_float} * {numb_2_float} = {numb_1_float * numb_2_float}')
    else:
        print('Operador não suportado!')
        continue

    sair = input('Gostaria de sair? ').lower()

    if sair == "sim" or sair == "sair":
        break