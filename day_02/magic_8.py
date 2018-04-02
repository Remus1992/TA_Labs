import random

responses = ["It is decidedly so",
             "Without a doubt",
             "Yes definitely",
             "You may rely on it",
             "As I see it, yes",
             "Most likely",
             "Outlook good",
             "Yes",
             "Signs point to yes",
             "Reply hazy try again",
             "Ask again later",
             "Better not tell you now",
             "Cannot predict now",
             "Concentrate and ask again",
             "Don’t count on it",
             "My reply is no",
             "My sources say no",
             "Outlook not so good",
             "Very doubtful",
             "It is certain"]


def magic_eight_ball():
    while True:
        stay_or_play = input('Would you like your fortune told? (y/n): ')
        if stay_or_play == 'y':
            query = input('What would you like to know?: ')
            if len(query) > 0:
                print(random.choice(responses))
            else:
                print("Sorry, didn't get that.")
        elif stay_or_play == 'n':
            print("Goodbye")
            break

        else:
            print("not a valid option")

magic_eight_ball()
