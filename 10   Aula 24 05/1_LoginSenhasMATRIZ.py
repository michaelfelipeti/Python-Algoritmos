import random
#Linha 0 = Login
#Linha 1 = Senhas
valores=[["a","ab","abc","abcd"],["1","12","123","1234"]]
tentativas = 1
aleatorio = random.randint(0,len(valores[0])-1)
print(valores[0][aleatorio])
tentSenha=input("Digite a senha correspondente ao login:\n")
while tentativas <3:
    if tentSenha == valores[1][aleatorio]:
        print("Acesso Liberado!")
        break
    print("Senha incorreta! Tente novamente!!")
    tentativas = tentativas + 1
    tentSenha=input("Digite a senha correspondente ao login:\n")
if tentSenha != valores[1][aleatorio]:
    print("Acesso Negado!")
