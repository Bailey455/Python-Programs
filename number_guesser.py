import random

num = random.randint(0,100)
print(num)

userInput = int(input("Please input a number from 1 - 100: "))


while userInput != num:
    if(userInput > num):
        userInput = int(input("Input a lower number: "))
    elif(userInput < num):
        userInput = int(input("Input a higher number: "))

if(userInput == num):
        print("you got the number!")






