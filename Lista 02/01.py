a = int(input("Insira o primeiro lado do triangulo: "))
b = int(input("Insira o segundo lado do triangulo: "))
c = int(input("Insira o terceiro lado do triangulo: "))
if(a + b >  c and a + c > b and c + b > a):
    if(a == b and b == c):
        print("Isso é um triangulo equilátero!")
    elif(a == b and b!=c):
        print("Isso é um triangulo isósceles!")
    elif(a == c and c!=b):
        print("Isso é um triangulo isósceles!")
    elif(b == c and c != a):
        print("Isso é um triangulo isósceles!")
    elif(b != a and b != c and a !=c):
        print("Isso é um triangulo escaleno!")
else:
    print("Isso não é um triangulo")
