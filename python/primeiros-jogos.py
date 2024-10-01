
import random

palavras = ["Guilherme", "Isael", "Diego", "Elias"]

PalavrasEscolhidas = random.choice(palavras)

print(PalavrasEscolhidas)

l = input("Informe-uma-letra ")
for letra in PalavrasEscolhidas:
    if(l == letra):
     print("A letra " + str(l) + " Esta na posição " + str(PalavrasEscolhidas.index(l)+ "latras"))
     print("palavra:"+" ".join("letraescolhida"))

l = input("informe uma letra")
letraescolhida = ["_"]* len ("letrasescolhida")
quantidade_de_erro = len (PalavrasEscolhidas)-1
meu_error = 0