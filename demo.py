import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("🎮 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_input = input("Enter your guess: ")

        # Check if input is a number
        if not user_input.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < number_to_guess:
            print("📉 Too low! Try again.")
        elif guess > number_to_guess:
            print("📈 Too high! Try again.")
        else:
            print(f"✅ Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guess_the_number()

