#Python Fundamentals
#---------------------
#Intro to Python

print("Hello World!")
print("My name is Ala Ganesh")
print("I'm learning Python")
print("My career goal is Data Analyst")
#---------------------------------------

#Variables
student_name = "Ganesh"
student_age = 23
student_cgpa = 7.70
print(student_name)
print(student_age)
print(student_cgpa)

college_name = "Bharath University"
graduation_year = 2026
software_language = "Python"
print(college_name)
print(graduation_year)
print(software_language)
#-----------------------------------

#Data Types
name = "Ala Ganesh"
age = 23
cgpa = 7.70
year = 2026
print(type(name))
print(type(age))
print(type(cgpa))
print(type(year))
#------------------

#Input and Type Conversions
age = int(input("Enter Your Age: "))
print("Your Age is ", age)
print(type(age))

#Type Conversions (int)
number = input("Enter a Number: ")
number = int(number)
print(number + 10)
#Type Conversions (float)
price = input("Enter MRP: ")
price = float(price)
print(price)
print(type(price))
#Type Conversions (str)
age = 23
age = str(age)
print(type(age))
#-------------------------

#Arithmetic Operators
a = 10
b = 20
print("Addition: ", a+b)
print("Subraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)
print("Floor Division: ", a//b)
print("Remainder: ", a%b)
print("Power: ", a**b)
#---------------------------------