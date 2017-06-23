def l():
    print()

def lernumeros():
   z1=int(input("Informe a medida do 1° lado do Triangulo: "))
   z2=int(input("Informe a medida do 2° lado do Triangulo: "))
   z3=int(input("Informe a medida do 3° lado do Triangulo: "))
   return(z1,z2,z3)

def calculo(z1,z2,z3):
    if z1 == z2 == z3:
        l()
        result=("O Triângulo é do tipo: Equilatero")
    elif (z1 == z2 != z3) or (z1 == z3 != z2) or (z3 == z2 != z1):
        l()
        result=("O Triângulo é do tipo: Isóceles")
    else:
        l()
        result=("O Triângulo é do tipo: Escaleno")
    return(print(result))

print("#-#"*5," Verificando Tipos de Triângulos ","#-#"*5)
(a,b,c)=lernumeros()
calculo(a,b,c)