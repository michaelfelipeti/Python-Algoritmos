'''
o programa anterior, deve informar ao final o aluno com maior e menor imc.
'''
nome=[]
PesoA=[]
AlturaA=[]
imcA=[]
mediaP= 0
mediaA= 0
mediaIMC=0
maiorimc=0
maiorimcnome="a"
menorimc=0
menorimcnome="a"
quant=int(input("Informe a quantidade de alunos da turma: "))
    #Enntrada de Dados e Calculo IMC
for i in range(quant):
    nome.append(input("Digite o nome do aluno: "))
    PesoA.append(float(input("Digite o peso: ")))
    AlturaA.append(float(input("Digite a altura: ")))
    imcA.append(PesoA[i]/(AlturaA[i]**2))
    #Calculo das medias e procura do maior e menor IMC
menorimc=imcA[0]
for i in range(quant):
    mediaP=mediaP+PesoA[i]
    mediaA=mediaA+AlturaA[i]
    mediaIMC=mediaIMC+imcA[i]
    if (imcA[i] > maiorimc):
        maiorimc=imcA[i]
        maiorimcnome=nome[i]
    if (imcA[i] < menorimc):
        menorimc=imcA[i]
        menorimcnome=nome[i]
mediaP=mediaP/quant
mediaA=mediaA/quant
mediaIMC=mediaIMC/quant
    #Saida
print("A média dos Pesos é : %f"%mediaP)
print("A média das Alturas é: %f"%mediaA)
print("A média dos IMC's é: %f"%mediaIMC)
print("O Aluno %s é o dono do maior IMC, que é: %d"%(maiorimcnome,maiorimc))
print("O Aluno %s é o dono do maior IMC, que é: %d"%(menorimcnome,menorimc))
