from random import randint
x = 1
lista =[]
while(x <=10):
    lista.append(randint(1,100))
    x = x + 1
aux = lista[0]
x = 1
while(x <10):
    if(aux < lista[x]):
        aux = lista[x]
    x = x+1
print(lista)
print(aux)
