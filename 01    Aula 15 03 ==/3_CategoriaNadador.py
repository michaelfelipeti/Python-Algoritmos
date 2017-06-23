def categoria(x):
    print("O nadador faz parte da Categoria: %s"%x)

idade=int(input("Idade do nadador(a): "))
if idade >=5 and idade<8:
    x="Infantil A"
    categoria(x)
elif idade>=8 and idade <11:
    x = "Infantil B"
    categoria(x)
elif idade >=11 and idade <14:
    x = "Juvenil A"
    categoria(x)
elif idade >=14 and idade <18:
    x = "Juvenil B"
    categoria(x)
elif idade >=18:
    x = "Adulto(a)"
    categoria(x)
else:
    print("Idade insuficiente para entrar em uma das Categorias!")