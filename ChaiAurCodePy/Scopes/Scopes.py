username="chaiaurcode" # Global varibale
def test():
    pass
    #scope

def func():
    #username="chai"    # Scope
    print(username)



# print(username)
# func()



x=99 # Global
# def func2(y):
#     z=x+y
#     return z

# result=func2(1)
# print(result)


# def func3():
#     global x  # overright global varibale 
#     x=12
# func3()
# print(x)


def f1():
    x=88
    def f2():
        print(x)
    f2()
f1()
