print("Digite três números aleatórios")
i = 0
n = [0,0,0]
while i<3:
    n[i] = int(input("digite o numero: "))
    i = i+1


'''n1=int(input("Insira um número:"))
n2=int(input("Insira um número:"))
n3=int(input("Insira um número:"))'''

if n[0]<n[1] & n[1]<n[2]:
    print("Os números inseridos foram:",n[0],n[1],n[2])
elif n[0]<n[2] & n[2]<n[1]:
    print("Os números inseridos foram:",n[0],n[2],n[1])
elif n[1]<n[2] & n[0]<n[2]:
    print("Os números inseridos foram:",n[1],n[0],n[2])
elif n[1]<n[2] & n[2]<n[0]:
    print("Os números inseridos foram:",n[1],n[2],n[0])
elif n[2]<n[0] & n[0]<n[1]:
    print("Os números inseridos foram:",n[2],n[0],n[1])
else:
    print("Os números inseridos foram:",n[2],n[1],n[0])



