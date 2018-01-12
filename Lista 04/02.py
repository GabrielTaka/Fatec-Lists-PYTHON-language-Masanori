from random import randint
lista = []
lista1 = []
lista2 = []
x = 0

while(x < 20):
    lista.append(randint(1,100))
    if(lista[x]%2==0):
        lista1.append(lista[x])
    else:
        lista2.append(lista[x])
    x = x + 1    



print(lista)    
print("Pares: ",lista1)
print("Impares: ",lista2)
