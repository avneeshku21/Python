
#*Python generators are a single way of creating iterators
# Genrator  ek normal function but yha return k jgh yield keyword hota hai
# aur call krne par ek generator object deta hai(Next chla iterate kr skte hai)

# Why use Itreator
#For ex- 
# x=range(10000)
# for i in x:
#   print(i**2)

# def gen_demo():
    
#     yield "first statement"
#     yield "second statement"
#     yield "third statement"

# def square(num):
#     for i in range(1,num+1):
#         yield i**2


#*****Example
# def mera_range(start,end):
    
#     for i in range(start,end):
#         yield i
# for i in mera_range(15,26):
#     print(i)