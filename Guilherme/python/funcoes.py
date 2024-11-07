#criar uma function para exportar nome python

...

#function
def imprimir(texto="Calcule sua média"):
    print(texto)
def media(n1, n2, n3):
    media =  (n1+n2+n3)/3
    print(media)


imprimir()

n1 = float(input("NOta 1: ")) 
n2 = float(input("NOta 2: ")) 
n3 = float(input("NOta 3: ")) 

media(n1, n2, n3)