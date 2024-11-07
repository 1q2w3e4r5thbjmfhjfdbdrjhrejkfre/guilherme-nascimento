
valor_saque = int(input("Quanto você quer? "))

notasde200 = valor_saque / 200
notasde100 = (valor_saque%200) / 100
notasde50 = (valor_saque%100) / 50
notasde20 = (valor_saque%50) / 20
notasde5 = (valor_saque%20) / 5

print("notas de : " + str(int(notasde200)))
print("notas de : " + str(int(notasde100)))
print("notas de : " + str(int(notasde50)))
print("notas de : " + str(int(notasde20)))
print("notas de : " + str(int(notasde5)))

