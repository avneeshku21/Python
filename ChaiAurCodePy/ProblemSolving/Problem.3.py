#password checker

password="Avneesh0021"
if len(password)<6:
    strength="weak"
elif len(password)>6:
    strength="strong"
else:
    print("Enter again")

print(strength)
