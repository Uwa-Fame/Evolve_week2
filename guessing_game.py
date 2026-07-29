
# my secret number
secret_number = 28

# stored three guesses
# guess1 = 28
# guess2 = 78
# guess3 = 28
guess1 = int(input("Enter your first Guess "))
guess2 = int(input("Enter your Second Guess "))
guess3 = int(input("Enter your third Guess "))

def check_guess(secret_number, guess):
    """ this function will check if the inputs stored on the Variables
    (guess1, guess2 and guess3) respectively to return the correct Value"""
    if guess > secret_number:
        return "Too high"
    elif guess < secret_number:
        return "Too low"
    else:
        return "correct!"

# testing to see if the programm is working
print(f"Guess 1: {check_guess(secret_number, guess1)}")
print(f"Guess 2: {check_guess(secret_number, guess2)}")
print(f"Guess 3: {check_guess(secret_number, guess3)}")