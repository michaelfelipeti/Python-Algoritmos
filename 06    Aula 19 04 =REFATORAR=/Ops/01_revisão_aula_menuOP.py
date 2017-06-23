
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
''' Variável Opção'''
op=int(input("Selecione uma das opções = Soma digite [1] - Maior [2] - Média [3] - Média [4]"))
''' Váriavel Resultado e Cauculo '''
r=(n1+n2+n3)
''' Variavel Média e Cauculo '''
med=r/3

''' Seria melhor ter utilizado o Elif após o primeiro IF / Rever exerxício 3_Num_Aleatório da Aula 22_03 '''
''' Calculo Maior número'''
if n1>n2 and n1>n3:
    M=n1
if n2>n3 and n2>n3:
    M=n2
if n3>n2 and n3>n2:
    M=n3

''' Calculo Menor número '''
if n1<n2 and n1<n3:
    m=n1
if n2<n3 and n2<n3:
    m=n2
if n3<n2 and n3<n2:
    m=n3

if op==1:
    print("A soma dos 3 números é: ,"r)
if op==2:
    print ("O maior número é: ",M)
if op==3:
    print("O menor número é: ",m)
if op==4:
    print("A média é: ",med)

'''
CÓDIGO V1: http://dontpad.com/algoritmo_aula19_04_cod1_v1
CÓDIGO V2:
'''

