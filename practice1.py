import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize a variable to keep track of the number of guesses
guess_count = 0

# Start the guessing loop
while True:
    # Ask the user for a guess
    guess = int(input("Guess the number between 1 and 100: "))

    # Increment the guess count
    guess_count += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} correctly in {guess_count} guesses.")
        break  # Exit the loop if the guess is correct
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
