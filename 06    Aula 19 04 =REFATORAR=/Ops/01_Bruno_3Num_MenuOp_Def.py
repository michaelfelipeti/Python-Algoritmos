def soma(n1,n2,n3):
   s=n1+n2+n3
   print(s)

def maior(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(a)
    elif n2>n1 and n2>n3:
        print(b)
    else:
        print(c)

def menor(n1,n2,n3):
    if n1<n2 and n1<n3:
        print(a)
    elif n2<n1 and n2<n3:
        print(b)
    else:
        print(c)

def media(n1,n2,n3):
    med=(n1+n2+n3)/3
    print(med)

a=int(input("Insira o primeira número:"))
b=int(input("Insira o segundo número:"))
c=int(input("Insira o terceiro número:"))

op=int(input("Escolha uma opção. Instruções: 1 - soma dos número, 2 - exibe o maior dos número, 3 - exibe o menor dos números, 4 - média dos números: "))

while op<0 or op>4:
    op=int(input("Opção inválida. Escolha uma opção. Instruções: 1 - soma dos número, 2 - exibe o maior dos número, 3 - exibe o menor dos números, 4 - média dos números: "))

if op==1:
    soma(a,b,c)
elif op==2:
    maior(a,b,c)
elif op==3:
    menor(a,b,c)
elif op==4:
    media(a,b,c)
else:
    print("Opção inválida")
