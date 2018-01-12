mercadoria = float(input("Digite o preço da mercadoria: "))
percent = int(input("Digite a porcentagem de desconto: "))
desconto = mercadoria * (percent/100)
print("O valor atual é de:", mercadoria - desconto)
