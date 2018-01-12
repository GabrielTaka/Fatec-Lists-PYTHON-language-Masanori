n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número:  "))
mdc = n1
while n1 % mdc != 0 or n2 % mdc != 0:
    mdc = mdc - 1
print ("MDC de %d e %d é = %d" %(n1, n2, mdc))
