import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 attempts to guess it correctly.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts_left = 5

    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        try:
            # Ask the player for a guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the correct number:", secret_number)
                break
            elif guess < secret_number:
                print("Try higher!")
            else:
                print("Try lower!")

            attempts_left -= 1

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    else:
        print("\nGame over! The correct number was:", secret_number)

# Run the game
guess_number_game()
