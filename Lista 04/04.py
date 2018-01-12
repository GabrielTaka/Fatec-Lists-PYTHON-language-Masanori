texto = '“The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”.'
texto = texto.lower()
texto = texto.replace("“", "")
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace(":", "")
texto = texto.split()
lista = []
x = 0
count = 0
while x < len(texto):
    if texto[x].startswith(tuple('python')) or texto[x].endswith (tuple('python')):
        lista.append(texto[x])
    x = x + 1    
print(lista)
