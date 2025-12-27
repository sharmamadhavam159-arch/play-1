import random
play= True
number = str(random.randint(10,20))
print("i willgenrate a number from 0 to 9, and youto guss the number 0ne digit at  a time ")
print("the game ends when you get 1 hero|")
while play:
    guess = input("give me your best guess| \n")
    if number == guess :
        print(" you win the game")
        print("the number was",number)
        break
    else:
        print("your guess isn't quite right' try again\n")