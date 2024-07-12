# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.
s=input("Enter String ")
term= input("Enter which char you want ")
counter=0
for i in s:
    if i==term:
        counter+=1
print('frequency',counter)

