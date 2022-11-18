50
import random
count = 6
num = random.randint(0,100)
number = int(input("Guess my number! (6 chance) : "))
for i in range (1,6):
    if num == number:
        print("Afarin!!!")
        break
    elif number < num:
        print("My number is bigger (↑) than yours!")
        number = int(input("Guess again! %s/6 : " %(i+1)))
        count -=1
    elif number > num:
        print("My number is smaller (↓) than yours!")
        number = int(input("Guess again! %s/6 : " %(i+1)))
        count -=1


if count == 1 and num != number:
    print("you lose :(")
    print ('the True awnser was :', num )
elif count == 1 and num == number:
    print("Afarin!!!")
# Matin Arjomand manesh