vCont=int(input("Digite o Valor da Conta: "))
vPag=int(input("Digite o Valor do Pagamento: "))

vTroc = vPag- vCont
troc50=0
troc20=0
troc10=0
troc5=0
troc2=0
troc1=0

while vTroc > 0:
    while vTroc>=50:
        troc50=troc50+1
        vTroc=vTroc-50

    while vTroc>=20:
        troc20=troc20+1
        vTroc=vTroc-20

    while vTroc>=10:
        troc10=troc10+1
        vTroc=vTroc-10

    while vTroc>=5:
        troc5=troc5+1
        vTroc=vTroc-5

    while vTroc>=2:
        troc2=troc2+1
        vTroc=vTroc-2

    while vTroc>=1:
        troc1=troc1+1
        vTroc=vTroc-1

print("O valor do Troco é de: R$",vTroc," .")
print("Seu troco terá: ",troc50," Notas de 50")
print("Seu troco terá: ",troc20," Notas de 20")
print("Seu troco terá: ",troc10," Notas de 10")
print("Seu troco terá: ",troc5," Notas de 5")
print("Seu troco terá: ",troc2," Notas de 2")
print("Seu troco terá: ",troc1," Notas de 1")

