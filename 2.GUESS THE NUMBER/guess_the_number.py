# Generate a number between 1 to 100

# # loop
# ask:to guess the number between 1 to 100
# if guessed number is greater than actual number 
#     print too high
# elif guessed number is smaller than actual number
#     print too low
# elif guessed number == actual number
#     print congratulations
#     terminate
# else print invalid choice

import random

gen_num=int(random.randint(1, 100))
while True :
    try:
        guess_num=int(input("Guess the number between 1 to 100: "))
    
        if guess_num > gen_num:
            print("Too high.")
        elif guess_num < gen_num:
            print("Too low.")
        else :
            print("Congratulations.")
            break
    except:
        print("Invalid choice")