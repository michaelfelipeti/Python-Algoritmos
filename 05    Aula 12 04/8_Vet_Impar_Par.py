def addvet(vet):
    for i in range(20):
        vet.append(int(input("Informe um %d° número: "%(i+1))))
def exibir():
    print()
    print("Vetor Completo: \n", vet)
    print("Vetor Par: \n", vetP)
    print("Vetor Impar: \n", vetI)

vet=[]
vetP=[]
vetI=[]
addvet(vet)
for a in range(20):
    if vet[a] % 2 == 0:
        vetP.append(vet[a])
    else:
        vetI.append(vet[a])
exibir()