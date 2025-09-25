# Conditional statements - code instructions that have different outcomes based on the input data
#input --> condition --> output

#conditional statement syntax
# if keyword: controls the conditon we want
# Else keyword: controls what happens if the condition is not met
# Elif keyword: controls multiple conditions


weather = input("How is the weather? ")
if weather == "sunny":
    print("Wear a t-shirt")
elif weather == "rainy":
    print("Wear a jacket")
elif weather == "snowy":
    print("Wear a coat")
else: 
    print('I do not understand that weather type')

password = input("Enter your password: ")
reinputpassword = input("Re-enter your password: ")
if password == reinputpassword:
    print("Access granted")
else:
    print("Access denied") 
    print("Try again")
    reinputpassword = input("Re-enter your password: ")
    if password == reinputpassword:
        print("Access granted")
    else:
     print("Access denied") 


vanilla = 1
chocolate = 10
strawberry = 10

def icecream(flavor):
    if flavor >= 1:
        print("we have that in stock.")
    elif flavor >= 1:
        print("we have chocolate in stock.")
    elif flavor >= 1:
        print("we have strawberry in stock.")
    else:
        print("we are out of stock.")

icecream(chocolate)


down = input('What down is it? ')
yards = input('How many yard do you need to get another first down? ')     
    
if down == 1 and yards <= 5:
    print("Run the ball")
elif down == 2 and yards <= 5:
    print("Run the ball")
elif down == 3 and yards <= 5:
    print("Play action pass")
else: down == 4 and yards <= 5
print("Punt the ball")


def age_check(age):
    if age >= 16:
        print("You are eligible to get your drivers permit.")
    else:
        print("You are not eligible to get your drivers permit.")

age = int(input("Enter your age: "))
age_check(age)


def positive_or_negative(number):
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

number = float(input("Enter a number: "))
positive_or_negative(number)


def grade_check(grade):
    if grade >= 90:
        print("You received an A.")
    elif grade >= 80:
        print("You received a B.")
    elif grade >= 70:
        print("You received a C.")
    elif grade >= 60:
        print("You received an F.")

grade = float(input("Enter your grade: "))
grade_check(grade)
