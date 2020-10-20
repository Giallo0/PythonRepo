#Fibonacci
num = 0
while num <= 0:
    num = int(input('N: '))
    if(num <=0):
        print('Il valore deve essere intero, positivo e diverso da 0') 
print(str(num) +' volte')

def fibonacci(n):
    #caso base
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(num):
    print(fibonacci(i))
