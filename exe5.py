"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_user = input('Digite apenas a hora: ')

try:
    hora_int = int(hora_user)
    bom_dia = hora_int >= 00 and hora_int <= 11
    boa_tarde = hora_int >= 12 and hora_int <= 17
    boa_noite = hora_int >= 18 and hora_int <= 23

    if bom_dia:
        print(f'Agora é {hora_int}Hrs e Bom dia')

    elif boa_tarde:
        print(f'Agora é {hora_int}Hrs e Boa tarde')

    elif boa_noite:
        print(f'Agora é {hora_int}Hrs e Boa noite')

    else:
        print('Hora não identificada, apenas das 00 as 23hrs')

except ValueError:
    print("Digite um numero inteiro!")
