print("Day-3: for loop")
for a in range(1,6):
    print (a)
print()

for i in range(5):
    print("Welcome to Python")
print()

for i in range(2,11,2):
    print(i)
print("---------------------")

print("while loop")
i = 1
while i <= 5:
    print(i)
    i = i+1
print("-----------------------")

print("break statement")
for i in range(1, 6):
    if i == 4:
        break 
    print(i) 
print("---------------------------")

print("continue statement")
for i in range(1,10):
    if i == 6:
        continue
    print(i)
print("----------------------")

print("Practical Examples")
for i in range(1,6):
    marks = int(input("Enter Student Marks: "))
    print("Student:", i, "Marks: ", marks)
print()

number = int(input("Enter Required Table Number: "))
for i in range(1,11):
    print(number, "X", i, "=", number*i)
print()

correct_pin = 1234
attempts = 0
while attempts < 3:
    pin = int(input("Enter Your Pin:  "))

    if pin == correct_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect Pin.")
        attempts = attempts + 1

if attempts == 3:
    print("Your Account has been Temporarily Locked")
print("-------------------------------------------------")

print("Practical Assignment")
print("print numbers from 1 to 20 using a for loop")
for i in range(1,21):
    print(i)
print()

print("All Even numbers between 1 and 50.")
for i in range (2,51,2):
    print(i)
print()

print("Multiplication Table")
number = int(input("Enter a Number: "))
for i in range(1,11):
    print(number, "X", i, "=", number*i)
print()

print("Using while loop, print from 10 down to 1")
i = 10
while i >= 1:
    print(i) 
    i -=1
print()

print("Marks of 5 students and calculates their average marks.")
total = 0
for i in range(1, 6):
    marks = int(input("Enter Marks: "))
    total = total + marks
average = total / 5
print("Total Marks:", total) 
print("Average Marks:", average)
print("-----------------------------------------------------------")

print("Knowledge Test")
print("Output of range(1, 5)")
for i in range(1,5):
    print(i)
#Output of range(1, 5)
#1
#2
#3
#4

print("Which loop is commonly used when the number of repetitions is known ?")
print("for loop")

print("What does `break` do  ?")
print("Stops the loop")

print("What does `continue` do ?")
print("Skips the current iteration")

print("What happens if you forget to update the counter in this loop: `i = 1; while i <= 5: print(i)`?")
print("It may run forever")
print("-----------------------------------------------------------------------------------------------------")

print("Challenge: Student Marks Analyzer")
print("Student Marks Analyzer")

mark1 = int(input("Enter Student 1 Marks: "))
mark2 = int(input("Enter Student 2 Marks: "))
mark3 = int(input("Enter Student 3 Marks: "))
mark4 = int(input("Enter Student 4 Marks: "))
mark5 = int(input("Enter Student 5 Marks: "))
  
total = mark1 + mark2 + mark3 + mark4 + mark5

average = total / 5

highest = max(mark1, mark2, mark3, mark4, mark5)
lowest = min(mark1, mark2, mark3, mark4, mark5)

print("----------------------")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)