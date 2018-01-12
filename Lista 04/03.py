from random import randint

lista1 = []
lista2 = []
lista = []
x = 0

while(x < 10):
    lista1.append(randint(1,100))
    lista2.append(randint(1,100))
    lista.append(lista1[x])
    lista.append(lista2[x])
    x+=1


print(lista1)
print(lista2)
print(lista)                  

