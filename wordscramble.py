import random

re = 0


def loopstuff():
            print("Try Again?")
            print("Y/N?")
            again = input()
            if again == "Y" or again == "y":
                game()
            else:
                if again == "N" or again == "n":
                   print("Good Bye")
                else: loopstuff() 

def game():
    global re 
    test = random.randint(0,5)
    if test == 0:
       word = 0
    elif test == 1:
        word = 1
    elif test == 2:
        word = 2
    elif test == 3:
        word = 3
    elif test == 4:
        word = 4
    elif test == 5:
        word = 5
    words = ["Snake","Elephant","Biology","Plant","Monkey","Bird"]
    test = words[word]
    convertingstring = list(test)
    random.shuffle(convertingstring)
    scrambled = "".join(convertingstring)
    
    print(scrambled)
    anwser = input("Anwser: ")
    if anwser == test or anwser == test.lower():
            print("Nice job")
            loopstuff()
    else: 
        print("Not correct")
        if re < 6:
            re = re + 1
            game()
        else:
            loopstuff()
            
game()
