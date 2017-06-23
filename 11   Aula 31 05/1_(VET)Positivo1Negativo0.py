def troca(vet):
    for i in range(len(vet)):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet
vet=[]
for i in range(5):
    vet.append(int(input("Informe um número: ")))
troca(vet)
print(vet)