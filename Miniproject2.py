weeknum = 1
weeks = 1
grade = 0
print("Choose a subject")
print("Math\nHistory\nCoding\nScience\nEnglish")

subject = input("subject: ")

if subject == "Math" or subject == "math":
    subject2 = "Math"
elif subject == "Coding" or subject == "coding":
        subject2 = "Coding"
elif subject == "Science" or subject == "science":
        subject2 = "Science"
elif subject == "English" or subject == "english":
        subject2 = "English"

while weeks < 18: 
    if grade/17 > 100: grade = 100
    grade = int(input(f"Grade for week {weeks}: ")) + grade
    weeks = weeks + 1
else: print(f"Your grade average is " + str(grade/17))

gradeletter = ""

figrade = grade/17
if figrade <= 50 and figrade < 60: print(f"Your letter grade is an F-")
if figrade <= 50 and figrade < 60: gradeletter = "F-"
if figrade >= 50 and figrade < 60: print(f"Your letter grade is an F") 
if figrade >= 50 and figrade < 60: gradeletter = "F"
if figrade >= 60 and figrade < 70: print(f"Your letter grade is an D") 
if figrade >= 60 and figrade < 70: gradeletter = "D"
if figrade >= 70 and figrade < 80: print(f"Your letter grade is an C")
if figrade >= 70 and figrade < 80: gradeletter = "C"
if figrade >= 80 and figrade < 90: print(f"Your letter grade is an B") 
if figrade >= 80 and figrade < 90: gradeletter = "B"
if figrade >= 90 and figrade < 100: print(f"Your letter grade is an A") 
if figrade >= 90 and figrade < 100: gradeletter = "A"       
if figrade >= 100: print(f"Your letter grade is an A+") 
if figrade >= 100: gradeletter = "A+"

if gradeletter == "F-":
        print(f"Failed {subject2} Big time")
if gradeletter == "F":
        print(f"Failed {subject2}")
if gradeletter == "D":
        print(f"Kinda failed {subject2}")
if gradeletter == "C":
        print(f"Barely past {subject2}")
if gradeletter == "B":
        print(f"Nice Job, you passed {subject2}")
if gradeletter == "A":
        print(f"You did great in {subject2}")
if gradeletter == "A+":
        print(f"Perfect score in {subject2}")
