a=int(input("Insira o primeira número:"))
b=int(input("Insira o segundo número:"))
c=int(input("Insira o terceiro número:"))

op=int(input("Escolha uma opção. Instruções: 1 - soma dos número, 2 - exibe o maior dos número, 3 - exibe o menor dos números, 4 - média dos números "))

if op==1:
    r=a+b+c
    print(r)
elif op==2:
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
elif op==3:
    if a<b and a<c:
        print(a)
    elif b<a and b<c:
        print(b)
    else:
        print(c)
elif op==4:
    md=(a+b+c)/3
    print(md)
else:
    print("Opção inválida")
