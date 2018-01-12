while True:
    nome = str(input("Insira seu nome: "))
    senha = str(input("Insira sua senha: "))
    if(senha == nome):
        print("A senha não pode ser igual ao seu nome")
    else:
        break;
