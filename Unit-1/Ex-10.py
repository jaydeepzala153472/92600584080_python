def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

#result=factorial(5)#5*4*3*2*1
#print('factorial is:',result)

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

num=9
for i in range(num):
    print(fib(i),end=" ")
 
