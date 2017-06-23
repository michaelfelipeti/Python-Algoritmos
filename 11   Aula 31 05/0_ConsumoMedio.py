kilometragemV = float(input("Informe a Kilometragem atual do Carro: "))
print()
print("."*20)
print("Próximo abastecimento...")
print("."*20)
print()
kilometragemN= float(input("Informe a Kilometragem atual do Carro: "))
combustivel = float(input("Informe a quantidade em L para encher o tanque: "))
km = kilometragemN - kilometragemV
custo = km/combustivel
print()
print("Consumo médio (km/l): ",custo)
