#1/1!+2/2!+3/3!..... nth
n=int (input('enter a number'))
result=0
fact=1

for i in (1,n+1):
    fact=fact*i
    result=result+i/fact
    print(result)
