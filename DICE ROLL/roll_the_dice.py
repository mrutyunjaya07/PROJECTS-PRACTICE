#loop
# asking : the user to roll the dice ?
# If user enters y :
#     generate a random number
#     print the number
# If user enters n :
#     print thank you message
#     terminate
# else :
#     print invalid choice

import random

while True :
    choice=input("Do you want to roll the dice ? (y/n): ").lower()
    if choice=='y':
        die1=random.randint(1, 6)
        print(f"{die1}")
    elif choice=='n':
        print("Thanks for playing.")
        break
    else:
        print("Invalid choice !!")
        