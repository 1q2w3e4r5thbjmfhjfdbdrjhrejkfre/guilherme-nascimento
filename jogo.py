import random

def escolher_palavra():
    palavras = ['olga', 'leonel', 'bruno', 'macaco', 'manel']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogar():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra.")

    while tentativas_restantes > 0:
        print("\n" + exibir_palavra(palavra, letras_corretas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if palpite in palavra:
            letras_corretas.add(palpite)
            if set(palavra) == letras_corretas:
                print("\nParabéns! Você adivinhou a palavra:", palavra)
                break
        else:
            letras_erradas.add(palpite)
            tentativas_restantes -= 1

        if tentativas_restantes == 0:
            print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogar()

    