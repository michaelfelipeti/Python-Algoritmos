qnt = int(input("Quantidade de idades a serem calculadas: "))
for i in range (qnt):
    idade = int(input("Informe a idade: "))
    if idade > maior:
        maior = idade
print(maior)
