import time
import os

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Mac and Linux (posix-compliant systems)
        _ = os.system('clear')

def game():
    score = 0
    print("Question 1: What is the capital of France?")
    answer1 = input("a) Berlin\nb) Madrid\nc) Paris\nd) Rome\nYour answer: ")
    if answer1 == "c":
        score = score + 1
    print("Question 2: What is 2 + 2?")
    answer2 = input("a) 3\nb) 4\nc) 5\nd) 6\nYour answer: ")
    if answer2 == "b":
        score = score + 1
    print("Question 3: What is the largest planet in our solar system?")
    answer3 = input("a) Earth\nb) Jupiter\nc) Mars\nd) Saturn\nYour answer: ")
    if answer3 == "b":
        score = score + 1
    print("Question 4: Who wrote 'Romeo and Juliet'?")
    answer4 = input("a) Charles Dickens\nb) Mark Twain\nc) William Shakespeare\nd) Jane Austen\nYour answer: ")
    if answer4 == "c":
        score = score + 1
    print("Question 5: What is the boiling point of water?")
    answer5 = input("a) 90°C\nb) 100°C\nc) 110°C\nd) 120°C\nYour answer: ")
    if answer5 == "b":
        score = score + 1
    print("Drumroll please!")
    time.sleep(1) 
    print("da")
    time.sleep(1) 
    print("Da")
    time.sleep(1) 
    print("DA")
    time.sleep(1) 
    print("DA!")
    time.sleep(2)
    print(f"Your total score is: {score} out of 5")
    if score == 1:
        print("✌️ 🫩  maybe next time twin.....")
    if score == 0:
        print("🤦‍♂️")
        time.sleep(2)
        print("This not you gng 👨‍🎓....")
        time.sleep(2)
        print("✌️ 😭")
    if score == 2:
        print("2 out of 5 in the big 2025 💀💀💀🥀🥀🥀😭 🙏")
    if score == 3:
        print("😛 so close.....")
    if score == 4:
        print("🫵 Wabi Sabi")
        time.sleep(2)
        print("🖖🫩")
    if score == 5:
        print("WE 🫵  👁 👅 👁 👈 got 5/5")
    time.sleep(3)
    print("Play again? ")
    answer = input("Yes or No ")
    if answer == "No" or answer == "no" or answer == "n" or answer == "N":
        print("Ok bye 👋")
    else:
        print("Too bad 😛")
        time.sleep(2)
        print("Do you really want to play again?")
        time.sleep(0.5)
        answer = input("Yes or No ")
        if answer == "No" or answer == "no" or answer == "n" or answer == "N":
            print("Ok bye 👋")
        else:
            clear_terminal()
            game()
game()
