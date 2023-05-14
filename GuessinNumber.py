import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number greater than 0.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randrange(0, top_of_range)

while True:
    user_guess = input('Make a Guess: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess == random_number:
            print("You got it!")
        else:
            print("You got it wrong!")
