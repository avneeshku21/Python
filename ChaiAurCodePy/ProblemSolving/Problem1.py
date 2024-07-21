#Age Group Categorization
age=int(input("Provide valid age : "))
if age==13:
    print("child")
elif age>13:
    print("Teenage")
elif age<60:
    print("Senior")

elif(age>100):
    print("Enter valid age")
else:
    print("try aagin")