'''
x = 0
x = int(input("Digite um número entre 1 e 10: "))

while (x>10):
    x=int(input("Erro, digite um número entre 0 e 10: "))

print (x,"x 1 =",x*1)
print (x,"x 2 =",x*2)
print (x,"x 3 =",x*3)
print (x,"x 4 =",x*4)
print (x,"x 5 =",x*5)
print (x,"x 6 =",x*6)
print (x,"x 7 =",x*7)
print (x,"x 8 =",x*8)
print (x,"x 9 =",x*9)
print (x,"x 10 =",x*10)
'''

# ------------------------ C O M   W H I L E ------------------------
n = int(input("Digite um valor entre 0 e 10: "))
x = 0

while (n>10):
    n = int(input("Erro, digite um valor entre 0 e 10: "))

while (x<=10):
#    print(n,"x",x,"=",n*x)
    print("%d x %d = %d"  %(n,x,n*x))
    x = x + 1


'''
n=int(input("Insira um número de 1 até 10: "))
while n>10:
    n=int(input("Erro,Insira um número de 1 até 10: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
'''
