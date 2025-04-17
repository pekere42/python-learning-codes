import random

print("🎯 Welcome to the Number Guessing Challenge!")

def guessing_game():
    choosen_number = random.randint(1, 100)

    while True:
        guessed_number = input("Please guess a number between 1 and 100 (or type 'quit' to exit): ").strip()

        if guessed_number.lower() == "quit":
            print("Game exited. See you next time!")
            break

        if guessed_number == "":
            print("❗ You didn't enter anything. Try again.")
            continue

        try:
            guess = int(guessed_number)
            if guess < 1 or guess > 100:
                print("⛔ Number must be between 1 and 100.")
                continue

            if guess > choosen_number:
                print("🔻 Too high! Try a smaller number.")
            elif guess < choosen_number:
                print("🔺 Too low! Try a bigger number.")
            else:
                print("🎉 Congratulations! You guessed the number!")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a number.")

guessing_game()

