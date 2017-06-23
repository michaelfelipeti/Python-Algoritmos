def condicao(sexo,imc):
    if   sexo=="M" and imc<19.1 or sexo=="H" and imc<20.7:
        situacao="Abaixo do peso"
    elif sexo=="M" and imc >= 19.1 and imc < 25.8   or   sexo=="H" and imc >=20.7 and imc<26.4:
        situacao="Peso normal"
    elif sexo=="M" and imc >= 25.8 and imc < 27.3   or   sexo=="H" and imc >=26.4 and imc<27.8:
        situacao="Acima do peso"
    elif sexo=="M" and imc >= 27.3 and imc < 32.3   or   sexo=="H" and imc >=27.8 and imc<31.1:
        situacao="Acima do peso ideal"
    return(situacao)

sexo=input("Informe seu Sexo. [M] P/Mulher e [H] P/Homem: ")
while sexo!="M" and sexo!="H":
    print("Dado inserido incorretamente!")
    sexo = input("Informe seu Sexo. [M] P/Mulher e [H] P/Homem: ")
peso=float(input("Informe seu peso: "))
altura=float(input("Informa sua altura:"))
imc=peso/(altura**2)

print()
print("="*20," Resultado do Exame ","="*20)
print("IMC = %.1f\nCondição Atual: %s"%(imc,(condicao(sexo,imc))))
print("="*62)