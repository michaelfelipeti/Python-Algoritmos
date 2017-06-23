num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))

while num1!=num2:
    if num1 < num2:
        num1 = num1 + 1
        print(num1-1)
    else:
        num2 = num2 + 1
        print (num2-1)
