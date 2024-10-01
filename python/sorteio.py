import random
pc_positivo = [20, 19, 18, 17, 16, 15, 14, 30, 29, 28, 27, 26, 25];
pc_dell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 23, 22, 21, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40];

def mistura(pc_dell, pc_positivo):
    pc_dell_misturado = random.shuffle(pc_dell)
    pc_positivo_misturado = random.shuffle(pc_positivo)

    troca = list(zip(pc_dell_misturado, pc_positivo_misturado))
    return troca

def imprimi(troca):
    for pc_positivo, pc_dell in troca:
        print("quem está usando o pc "+str(pc_positivo)+" vai usar o Pc"+str(pc_dell))