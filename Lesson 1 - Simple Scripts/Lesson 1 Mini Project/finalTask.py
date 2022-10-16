def find_secret_number(lower_value, upper_value):
    guess = int((lower_value + upper_value) / 2)
    print("Is your secret number " + str(guess) + "?")
    user_answer = input("Enter 'h' to indicate the guess is too high. "
                        "Enter 'l' to indicate the guess is too low. "
                        "Enter 'c' to indicate I guessed correctly.")
    if user_answer == 'h':
        return find_secret_number(lower_value, guess)
    elif user_answer == 'l':
        return find_secret_number(guess, upper_value)
    elif user_answer == 'c':
        return guess
    else:
        print("Sorry, I did not understand your input.")
        return find_secret_number(lower_value, upper_value)
    return 0 # You should erase this return...


def start_program():
    print("Please think of a number between 0 and 100!")
    ans = find_secret_number(0, 100)
    print("Game over. Your secret number was: " + str(ans))
