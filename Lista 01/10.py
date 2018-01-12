cigarros = int(input("Quantidade de cigarros fumados por dia: "))
anos = int(input("Anos em que se fuma cigarro: "))
resultado_cigarros = (cigarros * 10) / 60
resultado_cigarrosd = resultado_cigarros / 24
resultado_anos = (anos * 365) * resultado_cigarrosd

print("Tempo de vida perdido em dias: ",resultado_anos)
