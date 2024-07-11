rows = int(input("Enter number of rows: "))

for i in range(1,rows):
    for j in range(1,i+1):
        print("* ", end="")
    print() # for new line



row = int(input("Enter number of rows: "))

for i in range(row):
    for j in range(i+1):
        print(j+1, end="")
    print()