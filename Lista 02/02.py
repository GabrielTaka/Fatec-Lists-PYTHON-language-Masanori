ano = int(input("Digite o ano: "))
resultado = ano % 4
resultado2 = ano % 100
resultado3 = ano % 400
if (resultado3 and resultado3) == 0 and resultado2 != 0:
    print("O ano é bissexto!")
else:
    print("O ano nâo é bissexto!")
