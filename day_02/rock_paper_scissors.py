import random


def player_choice():
    user_choice = input("Rock, Paper, or Scissors: ").lower()
    # print(user_choice)
    return user_choice


def CPU_choice():
    CPU_Choices = ['rock', 'paper', 'scissors']
    CPU_choice = random.choice(CPU_Choices)
    print(CPU_choice)
    return CPU_choice


def game():
    while True:
        play_or_not = input("Would you like to play? (Y/N): ").lower()
        if play_or_not == 'y':
            CPU = CPU_choice()
            player = player_choice()
            if player == 'rock' and CPU == 'rock' or player == 'paper' and CPU == 'paper' or player == 'scissors' and CPU == 'scissors':
                print("CPU chose %s\nTIE.\n" % (CPU))

            elif player == 'rock' and CPU == 'scissors' or player == 'paper' and CPU == 'rock' or player == 'scissors' and CPU == 'paper':
                print("CPU chose %s\nPlayer Wins.\n" % (CPU))

            elif player == 'scissors' and CPU == 'rock' or player == 'rock' and CPU == 'paper' or player == 'paper' and CPU == 'scissors':
                print("CPU chose %s\nCPU Wins.\n" % (CPU))

            else:
                print('Duh no what happen? ¯\_(ツ)_/¯')
        elif play_or_not == 'n':
            print('Goodbye')
            break

        else:
            print('invalid option')


game()
