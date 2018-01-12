a = 80000
b = 200000
anos = 0
while a <= b:
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    anos = anos + 1
print( "Daqui %d anos a população de A será maior que a de B", anos)
print ("A população de A é de: %d" %a)
print ("A população de B é de: %d" %b)
