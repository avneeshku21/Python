# function with args
def summ_all(*args):
    #print(agrs) #it give tuple
    return sum(args)

print(summ_all(1,2,3))
print(summ_all(1,2,3,4,5,5))
print(summ_all(1,2,3,4,5,5,6,7,8))