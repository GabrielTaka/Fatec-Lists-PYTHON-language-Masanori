import os
os.system("clear")
statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
statement= statement.lower() 
statement= statement.replace(',',' ')
statement= statement.split() 
print(statement) 
lista2= []
for i in range(0,(len(statement))):
    if statement[i].startswith(tuple('python')) or statement[i].endswith(tuple('python')): 
        lista2.append(statement[i])
print ('\nlista 2 - lista com as palavras que começam ou terminam com uma das letras “python”:\n', lista2)
lista3= []
for y in range(0,(len(lista2))):
	if len(lista2[y]) >= 4:
		lista3.append(lista2[y])	
print ('\nlista 3: tem %d palavras com 4 caracteres ou mais: ' % (len(lista3)))
