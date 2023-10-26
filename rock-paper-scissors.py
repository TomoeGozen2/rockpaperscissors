import random


def shoot():
    options = ['rock','paper','scissors']
    global computer_choice 

    computer_choice = random.choice(options)


def human_choice():

    
    
    while True:
        shoot()
        global computer_choice
        user_input = input('Enter your choice. Rock, paper or scissors? ').lower()
        if user_input =='rock' and computer_choice == 'rock':
            print('Its a tie. Go again?')
            continue

        elif user_input =='rock' and computer_choice == 'paper':
            print('The user lost!')
            continue
        elif user_input == 'rock' and computer_choice == 'scissors':
            print('The human won!')
            break

        elif user_input =='paper' and computer_choice == 'paper':
            print('Tie. Try again?')
            continue
        elif user_input == 'paper' and computer_choice == 'scissors':
            print('The human lost. Again?')
            continue
        elif user_input == 'paper' and computer_choice == 'rock':
            print('The human won!')
            break
        
        elif user_input =='scissors' and computer_choice == 'scissors':
            print('Tie. Try again?')
            continue
        elif user_input == 'scissors' and computer_choice == 'rock':
            print('The human lost. Again?')
            continue
        elif user_input == 'scissors' and computer_choice == 'paper':
            print('The human won!')
            break

print('You are going to play a game of rock papper scissors against a computer')
human_choice()






