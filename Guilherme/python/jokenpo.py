
import random

jogada = int(input("ESCOLHA UMA OPÇÃO PLAYER:  [0 - PEDRA | 1 - PAPEL | 2 - TESOURA] "))

cpu = random.randint(0,2)

print(cpu) 

#Condições

#PLAYER ganhar
if jogada == 0 and cpu == 2:
    print("PLAYER VENCEU!")
if jogada == 1 and cpu == 0:
    print("PLAYER VENCEU!")
if jogada == 2 and cpu == 1:
    print("PLAYER VENCEU!")

#CPU ganhar
if jogada == 0 and cpu == 1:
    print("CPU VENCEU!")
if jogada == 1 and cpu == 2:
    print("CPU VENCEU!")
if jogada == 2 and cpu == 0:
    print("CPU VENCEU!")

#Empate!
if jogada == 2 and cpu == 2:
    print("Empate!")
if jogada == 0 and cpu == 0:
    print("Empate!")
if jogada == 1 and cpu == 1:
    print("Empate!")