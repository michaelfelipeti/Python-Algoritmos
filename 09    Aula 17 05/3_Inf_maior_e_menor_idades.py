qnt = int(input("Quantidade de idades a serem calculadas: "))
for i in range (qnt):
    idade = int(input("Informe a %dº idade: "%(i+1)))
    if i == 0:
        menor = idade
        maior = idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
print("Maior número digitado: %d"%maior)
print("Menor número digitado: %d"%menor)
