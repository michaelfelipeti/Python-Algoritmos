'''
Faça um algoritmo que leia dois números inteiros e exiba a média aritmética e exiba as mensagens a seguir de acordo com a média calculada.
entre 0 e 5,9 - Insuficiente
entre 6 e 6,9 - suficiente
entre 7 e 8,9 - Bom
entre 9 e 10 - Ótimo
'''
nota1=int(input("Digite a nota: "))
nota2=int(input("Digita a nota: "))
media=(nota1+nota2)/2

if media >=0 and media <6:
    print("Insuficiente!")
elif media >=6 and media <7:
    print("Suficiente!")
elif media >=7 and media <9:
    print("Bom!")
elif media >=9 and media <10.1:
    print("Ótimo!")
else:
    print("Media inconsistente")
