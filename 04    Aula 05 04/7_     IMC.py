'''
Faça um programa que o usuário informe a quantidade de alunos de uma turma, o sistema deve ler o peso e altura de cada aluno,
ao final informar a média dos pesos, alturas e imc.
'''
nome=[]
PesoA=[]
AlturaA=[]
imcA=[]
mediaP= 0
mediaA= 0
mediaIMC=0

quant=int(input("Informe a quantidade de alunos da turma: "))

for i in range(0,quant):
    nome.append(input("Digite o nome do aluno: "))
    PesoA.append(float(input("Digite o peso: ")))
    AlturaA.append(float(input("Digite a altura: ")))
    imcA.append(PesoA[i]/(AlturaA[i]**2))

for i in range(0,quant):
    mediaP=mediaP+PesoA[i]
    mediaA=mediaA+AlturaA[i]
    mediaIMC=mediaIMC+imcA[i]
mediaP=mediaP/quant
mediaA=mediaA/quant
mediaIMC=mediaIMC/quant

print("A média dos Pesos é : %f"%mediaP)
print("A média das Alturas é: %f"%mediaA)
print("A média dos IMC's é: %f"%mediaIMC)
