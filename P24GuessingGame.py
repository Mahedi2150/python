from random import randint

c=0
for x in range(1,6):
    guessNumber = int(input("Enter your guess between 1 to 5 :"))
    randomNumber = randint(1, 5)
    if guessNumber==randomNumber:
        print("You have Won!!!")
        c=c+1
    else:
        print("you have loss")
        print("Random Number was :",randomNumber)
print("\nTotal win :",c)