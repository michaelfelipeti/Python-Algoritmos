def addvet():
    vet.append(float(input("Informe um número: ")))
vet=[]
vetcontra=[]
cont = len(vet)
for i in range(10):
    addvet()
for a in range(10):
    vetcontra.append(vet[cont-1])
    cont = cont - 1
print(vetcontra)