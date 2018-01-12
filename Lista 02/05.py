n1 = int(input("Digite o primeiro nùmero: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("DIigite o terceiro número: "))
if n1 < n2 and n1 < n3:
    print("O número %d é o menor" %n1)
elif n2 < n1 and n2 < n3:
    print("O número %d é o menor" %n2)
elif n3 < n1 and n3 < n2:
    print("O número %d é o menor " %n3)
