import random

def guessing_game():
    # Generate a random number between 1 and 100
    num = random.randint(1, 100)
    guess = int(input("Guess the number! Enter a number between and including 1 and 100: "))
    count = 0

    # Continue to ask for input until the user guesses the number correctly
    # The user is also notified if the guess is too big or too small
    while guess != num:
        if guess > num:
            guess = int(input("That\'s not right, " + str(guess) + " is too big! Guess again: "))
        elif guess < num:
            guess = int(input("That\'s not right, " + str(guess) + " is too small! Guess again: "))

        # Add 1 to the count for each loop that the guess is incorrect
        count = count + 1

    # If the guess is correct the user is notified and the total number of guesses taken is given
    if guess == num:
        count = count + 1
        return "That\'s right! You took " + str(count) + " guess(es)"
