import random

def pulalinha():
    print()

num = random.randint(0,10)
chute = 20
t = 0
print ("\n" * 130)
while chute!=num:
    t = t+1
    chute = int(input("Digite seu chute: "))
    if chute > num:
        pulalinha()
        print("Erroww! Chutou muito pra cima fera")
    elif chute < num:
        pulalinha()
        print("Erroww! Chutou muito pra baixo fera")
    else:
        pulalinha()
        print("=" * 20, " Fim de Jogo ", "=" * 20)
        print("Acertou Mizeravi!!")
        print("Número total de tentativas: ",t)
        print("=" *55)

