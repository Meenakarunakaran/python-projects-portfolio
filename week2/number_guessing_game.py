import random
print("Welcome to the Number Guessing Game!")
while True:
    print("\nI have chosen a number between 1 and 100.")
    print("You have 7 chances to guess it!")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break   
        except ValueError:
            print("Please enter a valid number.")
    else:  
        print(f"Sorry, you ran out of chances! The number was {secret_number}.")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
