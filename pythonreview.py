# Question 1
def check_submissions():

    cw = input("Did you submit your class work? (yes/no): ")
    hw = input("Did you submit your homework? (yes/no): ")

    if cw == "yes" and hw == "yes":
        print("Great! You submitted both class work and homework.")
    elif cw == "yes" and hw == "no":
        print("You submitted class work but not homework.")
    elif hw == "yes" and cw == "no":
        print("You submitted homework but not class work.")
    else:
        print("You did not submit class work or homework.")

# Question 2
def reverse_string(s: str) -> str:
    """
    Return the given string in reverse order.
    Uses Python slicing to reverse the string.
    """
    return s[::-1]

def reverse_input():
    s = input("Type a word: ")
    print("Reversed:", reverse_string(s))

check_submissions()

reverse_input()


guessednumber = False
attempts = 0

# Question 3
def guess_number_game():
    guessednumber = False
while guessednumber == False:
    player = input("Pick a number between 1 and 10: ")
    if player == "7":
        print("You guessed the correct number!")
        guessednumber = True
        attempts += 1
        print("You took", attempts, "attempt(s) to guess the number.")
    else:
        if player < "7":
            print("Your guess is less than the number, try again.")
            attempts += 1
        else:
            print("Your guess is more than the number, try again.")
            attempts += 1
guess_number_game()
