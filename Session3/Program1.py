
#FInd the length of String Without using len()
# s=input("Enter String ")
# counter=0
# for i in s:
#     counter+=1
# print('Length',counter)

#Exact usename from give email
#eg if the emaik is avneeshkumar021@gmail.com
#then the user name should be avneeshkumar021

s=input("Enter String ")
pos =s.index('@')
print(s[0:pos])

