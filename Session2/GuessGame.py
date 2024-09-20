import random
jackpot=random.randint(1,100)
guess=int(input("Guess the Number: "))

while guess!=jackpot:
    if guess==jackpot:
       print("Right Guess")
    elif guess>jackpot:
        print("Thoda Jada Guess kro bhai")
    elif guess<jackpot:
        print("Thoda kam Guess krliya bhai")

    guess=int(input("Guess the Number: "))
else:
    print("Guess Number",guess)




    

   
    





