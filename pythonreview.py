# Question 1
def check_submissions():

    cw = input("Did you submit your class work? (yes/no): ").strip().lower()
    hw = input("Did you submit your homework? (yes/no): ").strip().lower()

    submitted_cw = cw in ("yes", "y", "true", "1")
    submitted_hw = hw in ("yes", "y", "true", "1")

    if submitted_cw and submitted_hw:
        print("Great! You submitted both class work and homework.")
    elif submitted_cw and not submitted_hw:
        print("You submitted class work but not homework.")
    elif submitted_hw and not submitted_cw:
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

# Question 3
def guess_number_game():
    guessednumber = False
while guessednumber == False:
    player = input("Pick a number between 1 and 10: ")
    if player == "7":
        print("You guessed the correct number!")
        guessednumber = True
    else:
        if player < "7":
            print("Your guess is less than the number, try again.")
        else:
            print("Your guess is more than the number, try again.")

guess_number_game()
