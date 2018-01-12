tam = int(input("Insira o tamanho em metros quadrados: "))
if(tam%54==0):
    latas =(tam/54)
    print("Você usará um total de %d latas que custará R$%d"% (latas, latas * 80))
else:
    latas =((tam//54)+1)
    print("Você usará um total de %d latas que custará R$%d"% (latas, latas * 80))
