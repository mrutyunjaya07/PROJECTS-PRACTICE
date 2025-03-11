# ask the user to make a choice
# If the choice is not valid
#     print error
# let the computer to make a choice
# print choices(emojis)
# Determine the winner
# ask the user if they want to continue
# If not 
#     terminate

import random
choices= ('r', 'p', 's')   #immutable
emojis={'r':'🪨','p':'📰', 's':'✂️'}

def get_user_choice():
    while True:
        user_choice=input("ROCK, PAPER, SCISSOR ?(r/p/s): ").lower()
        # if user_choice not in choices:
        #     print('Invalid choice !')
        #     continue
        # else :
        #     return user_choice
        if user_choice in choices:
            return user_choice
        else :
            print('Invalid choice !')

def display_choices(user_choice, comp_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[comp_choice]}")

def determine_winner(user_choice, comp_choice):
    if user_choice== comp_choice:
        print('Tie !!')
    elif ((user_choice=='r' and comp_choice=='s') or
        (user_choice=='s' and comp_choice=='p') or
        (user_choice=='p' and comp_choice=='r')) :
        print("You win !!")
    else :
        print("You lose !!")
            
        

def play_game():        
    while True:
        user_choice=get_user_choice()

        comp_choice=random.choice(choices)

        display_choices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)


        should_continue=input('Continue ?(y/n): ').lower()
        if should_continue=='n':
            print('Thanks for playing.')
            break
            
play_game()