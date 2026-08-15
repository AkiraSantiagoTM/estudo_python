"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero)
    par = numero_int % 2 == 0

    if par:
        print(f'O numero digitado {numero_int} é PAR')
    else:
        print(f'O numero digitado {numero_int} é IMPAR')

except:
    print('Digite um numero inteiro!')