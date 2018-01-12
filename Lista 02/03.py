peso = int(input("Peso: "))
if peso > 50:
    excesso = peso - 50
    multa = (peso - 50) * 4
    print("Excesso em kg", excesso)
    print("O senhor foi multado em R$%.2f senhor" % multa)
else:
    multa = 0
    print("O senhor nâo foi multado", multa)
