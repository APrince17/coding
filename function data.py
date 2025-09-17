# How to create a function that passes data
# step 1. Create a function definition
def bnbrefund(username, refundamount):
    print('sorry '+ username + ' for your cancellation')
    print('you will be refunded $' + str(refundamount))

# step 2. Call the function and execute the code inside the function
bnbrefund('jacob', 3000)

def birthday(name, birthday1):
    print('My name is ' + name)
    print('and my birth day is ' + str(birthday1))

birthday('Amir Prince', 'Febuary 25, 2008')



def dollarsintopennies(dollars):
   
    pennies = dollars * 100
    print('You have ' + str(pennies) + ' pennies')


dollar2 = 300

dollarsintopennies(dollar2)

def areaofrectangle(length, width):
    area = length * width * 0.5
    print('The area of the rectangle is ' + str(area) + ' square units')

areaofrectangle(5, 10) 

def areaofatriangle(length, width, height):
    area = length * width * height
    print('The area of the triangle is ' + str(area) + ' square units')

areaofatriangle(5, 10, 15)

def temperatureincelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    print('The temperature in fahrenheit is ' + str(fahrenheit),  ', degrees in celsius is '+ str(celsius))

temperatureincelsius(100)
