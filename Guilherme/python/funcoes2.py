#tempos de vida
def imprimir(texto=""):
    print(texto)
def vida(n1, n2):
    vida = (n1-n2)
    dias = 365 * vida
    horas = dias * 23.56
    print(vida)
    print(dias)
    print(horas)
imprimir()
n1 = float(input("que ano nasceu??: "))
vida(n1, 2024)