import random

def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = 0

    print("Try to guess the number, it must be between 1 and 100")

    # Continue asking for guesses until the correct number is guessed
    while guess != secret_number:
        # Prompt the user to enter their guess and convert it to an integer
        guess = int(input("Take a guess: "))

        # Check if the input is matching the secret number or not
        if guess < secret_number:
            print("Try again, this time it was too low")
        elif guess > secret_number:
            print("Try again, this time it was too high")
        else:
            print("Congrats! You've guessed it correctly!")

main()
