'''========================'''
diaAtual=14
mesAtual=6
anoAtual=2017
'''========================='''
diaUsuario=int(input("Informe seu dia de nascimento: "))
mesUsuario=int(input("Informe seu mes de nascimento: "))
anoUsuario=int(input("Informe seu ano de nascimento: "))

#Calculo de idade
if mesUsuario < mesAtual:
    anoIdade= anoAtual-anoUsuario
    mesIdade= mesAtual-mesUsuario
    diaIdade= 30 - (diaUsuario-diaAtual)
    if diaUsuario==diaAtual:
        diaIdade=1

elif mesUsuario > mesAtual:
    anoIdade= anoAtual-anoUsuario
    mesIdade= 12 -(mesUsuario - mesAtual)
    diaIdade= 30 - (diaUsuario-diaAtual)

elif mesUsuario == mesAtual:
    if diaUsuario > diaAtual:
        anoIdade= anoAtual-anoUsuario
        mesIdade= 1
        diaIdade= (diaUsuario-diaAtual)
    elif diaUsuario <= diaAtual:
        anoIdade= anoAtual-anoUsuario
        mesIdade= 12 -(mesUsuario - mesAtual)
        diaIdade = 30 - (diaUsuario-diaAtual)
        if diaUsuario==diaAtual and mesUsuario==mesAtual:
            anoIdade=anoIdade+1
            mesIdade=1
            diaIdade=1
            print("Feliz Aniversário :D")

print("Você tem:\n%d Anos\n%d Meses\n%d Dias"%(anoIdade,mesIdade,diaIdade))
