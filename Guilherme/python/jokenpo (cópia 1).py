import random

jogada = int(input("ESCOLHA UMA OPÇÃO PLAYER: [0 - PEDRA | 1 - PAPEL | 2 - TESOURA]: "))
cpu = random.randint(0,2)

#Player ganhar
if jogada == 0 and cpu == 2:
    print("Player Venceu!")
if jogada == 1 and cpu == 0:
    print("Player Venceu!")
if jogada == 2 and cpu == 1:
    print("Player Venceu!")

#CPU vencer
if jogada == 0 and cpu == 1:
    print("CPU Venceu!")
if jogada == 1 and cpu == 2:
    print("CPU Venceu!")
if jogada == 2 and cpu == 0:
    print("CPU Venceu!")

#Empate
if jogada == 0 and cpu == 0:
    print("Empate!")
if jogada == 1 and cpu == 1:
    print("Empate!")
if jogada == 2 and cpu == 2:
    print("Empate!")

#     import random

# jogada = int(input("ESCOLHA UMA OPÇÃO[ 0 - PEDRA | 1 - PAPEL | 2 - TESOURA ]"))

# CPU = random.randint(0,2)

# print (CPU)

# if (jogada == 0 and CPU == 2) or (jogada == 1 and CPU == 0) or (jogada == 2 and CPU == 1):
#     print("player venceu")

# elif (jogada == 2 and CPU == 0) or (jogada == 0 and CPU == 1) or (jogada == 1 and CPU == 2):
#     print("CPU venceu")

# else:
#     print("empate")



