def lerNumero():
    a=int(input("Digite um número Inteiro: "))
    return(a)

def soma(a,b,c):
    return(a+b+c)

def media(a,b,c):
    return(soma(a,b,c)/3)

def maior(a,b,c):
    if a>b and a>c:
        M=a
    elif b>a and b>c:
        M=b
    elif c>a and c>b:
        M=c
    return (M)

def menor(a,b,c):
    if a<b and a<c:
        M=a
    elif b<a and b<c:
        M=b
    elif c<a and c<b:
        M=c
    return (M)




n1=lerNumero()
n2=lerNumero()
n3=lerNumero()

print(soma(n1,n2,n3))
print(media(n1,n2,n3))
print(maior(n1,n2,n3))
print(menor(n1,n2,n3))

