dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

print("O número total de segundo é de {}".format(segundos + minutos * 60 + horas * 3600 + dias * 86400))
