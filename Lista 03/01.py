while True:
    nota = int(input("Insira uma nota entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        break;
    else:
        print("Nota inválida, digite novamente")
