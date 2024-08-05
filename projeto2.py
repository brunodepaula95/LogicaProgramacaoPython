#Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente. O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

import random

valor_aleatorio = random.randint(1,10)
Tentativas = 4
rodadas = 4



while True:
    chute = int(input("Digite um numero de 1 a 10   "))
    if chute == valor_aleatorio:
        print("Você acertou")
        break

    elif chute < valor_aleatorio:
        print("Tente um valor maior")

    elif chute > valor_aleatorio:
        print("Tente um valor menor")

    if rodadas == 0:
        print("Acabou suas tentativas")
        break

    rodadas -= 1