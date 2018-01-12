distancia = int(input("Quantidade km rodados: "))
dias = int(input("Dias alugados: "))
custo_dias = dias * 60
custo_km = distancia * 0.15
custo_final = custo_dias + custo_km
print("O valor é de: ", custo_final)
