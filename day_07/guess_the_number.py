import random

cpu = random.randint(1, 10)
print(cpu)

last_guess_target = 0
while True:
    guess = int(input("Number: "))
    current_guess_target = guess
    if guess == cpu:
        # print(last_guess_target)
        # print(current_guess_target)
        print("%s is right!" % guess)
        break
    elif guess > cpu:
        print("Last Guess: %s" % last_guess_target)
        distance = abs(last_guess_target) - abs(current_guess_target)
        abs_distance = abs(distance)
        if abs_distance == guess:
            print("Too high.")
        elif abs_distance != guess:
            if distance < 0:
                print("Distance from last guess: %s" % distance)
                print("You're too high and you're getting further away.")

            elif distance > 0:
                print("Distance from last guess: %s" % distance)
                print("Too high. Hold on though, you're getting there.")
        last_guess_target = current_guess_target

    elif guess < cpu:
        print("Last Guess: %s" % last_guess_target)
        # print(current_guess_target)

        distance = abs(last_guess_target) - abs(current_guess_target)
        abs_distance = abs(distance)
        if abs_distance == guess:
            print("Too low.")
        elif abs_distance != guess:
            if distance < 0:
                print("Distance from last guess: %s" % distance)
                print("You're too low but you're on the right tract.")

            elif distance > 0:
                print("Distance from last guess: %s" % distance)
                print("Too Low. Weirdly enough you're going the wrong way.")
        last_guess_target = current_guess_target

    else:
        print("Sorry. Try again.")
