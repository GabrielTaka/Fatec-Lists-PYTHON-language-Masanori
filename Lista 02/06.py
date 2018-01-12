ganho = int(input("Ganho por hora: "))
horas = int(input("Horas trabalhadas por mês: "))
sb = ganho * horas
ir =(sb * 11) / 100
inss = (sb * 8) / 100
sind = (sb * 5) / 100
sl = sb - ( ir + inss + sind)
print ("Salário bruto é de %.2f" %sb)
print ("Foram descontados R$%.2f do seu salário para o imposto de renda" %ir)
print ("Foram descontados R$%.2f do seu salário para o inss" %inss)
print ("Foram descontados R$%.2f do seu salário para o sindicato" %sind)
print ("R$%.2f é o seu salário líquido" %sl)
