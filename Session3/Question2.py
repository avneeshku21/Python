# rows = int(input("Enter number of rows: "))

# for i in range(1,rows):
#     for j in range(1,i+1):
#         print("* ", end="")
#     print() # for new line



# row = int(input("Enter number of rows: "))

# for i in range(1,row):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

rows = int(input('enter number of rows: '))
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(j,end='')
  for k in range(i-1,0,-1):
    print(k,end='')
  print()