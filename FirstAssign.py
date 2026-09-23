#Notes 9/16
age = int(input("enter your age"))

if age > 0 or age < 18:
print("you are a minor")

if age > 0 and name == "Messi"
print("you are a fan of messi!")
#== means compare while = means to set    and = one and the other have to be true for both of them to be true - if ones not then its all false. Ands accure before ors

age = 5
name = "Blah"

if (age > 0) and (name == "Messi") or (name == "Blah"): # this is the correct version with parenthases

gpa = 3.1

if gpa >= 3.0:
    print("you are eligable for the scholarship")  # 

      if name == "Marriot"
              print("congradualaations")

#Definite loop = We know how many times we want to run
#Infinant loop = We don't know how many times it will run

for counter in range(0, 101, 5): #Definite usually use i j or k instead of counter. The 2 has it count up by two all the way to 104 (its the incrament)
     print(counter)

#Indef loop right here
age = int(input("How old are you"))
print(age)

while age < 0:
     print("You can't be negative years old!")
     age = int(input("How old are you?")) #need this whole line to recive input

if (age == -16):
     break # This is a special condition and it will exit the loop

if (age == 15):
     continue

#print out day 1 appointment 1 - 5 then day 2. This is a loop inside of a loop

for i in range(1,4):
     for j in range(1,6):
          print(f"Day {i}, Appointment {j}")


