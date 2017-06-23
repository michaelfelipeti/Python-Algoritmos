import random

login=["a","ab","abc","abcd"]
senha=["1","12","123","1234"]
tentativas = 1

lEscolhido = random.randint(0,len(login)-1)
print(login[lEscolhido])

tentSenha=input("Digite a senha correspondente ao login:\n")
while tentativas <3:
    if tentSenha == senha[lEscolhido]:
        print("Acesso Liberado!")
        break
    print("Senha incorreta! Tente novamente!!")
    tentativas = tentativas + 1
    tentSenha=input("Digite a senha correspondente ao login:\n")

if tentSenha != senha[lEscolhido]:
    print("Acesso Negado!")
