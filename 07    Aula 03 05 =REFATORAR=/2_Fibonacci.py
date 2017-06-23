num=int(input("Digite o número para exibir a Sequencia: "))
pos1=1
pos2=1
atual=1
print("Esses são os elementos da sequencia de Fibonnaci até o número Digitado.")
print(pos1)
while atual<=num:
    print(atual)
    atual=pos1+pos2
    pos2=pos1
    pos1=atual
