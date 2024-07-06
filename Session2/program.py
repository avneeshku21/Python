#programe - find the sum of a 3 digit number
num= int(input("Enter a number"))
print(num)
 
a=num%10
num= num//10
b=num%10
num=num//10

c=num%10

print("Sum :" , a+b+c)