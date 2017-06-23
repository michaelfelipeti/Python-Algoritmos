ano=int(input("Digite um número para saber se é ou não Bissexto: "))
if (ano % 4==0) & (ano % 100!=0) | (ano % 400==0):
    print("O ano %d é Bissexto!"%(ano))
else:
    print("O ano %d não é Bissexto!"%(ano))
