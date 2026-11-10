print("Comparison Operators")
a = 20
b = 10
print(a == b)
print(a != b)
print(a > b)
print(a <b )
print(a >= b)
print(a <= b)
print("--------------")

print("Exercise")
maths = 85
science = 90
print(maths == science)
print(maths > science)
print(science > maths)
print(maths <= 85)
print("--------------")

print("Logical Operators")
print("AND")
maths = 90
science = 85
print(maths >= 50 and science >= 40)
print("OR")
maths = 88
english = 95
print(maths >= 60 or english >= 70)
print("NOT")
social = 85
hindi = 75
print(not social >= 86)
age = 20
print(not age >= 22)
print()
print("----------------------")

print("Real-World Example")
maths = 85
physics = 90
chemistry = 88
eligible = maths >= 75 and physics >= 80 and chemistry >= 85
print("Student Marks are: ",eligible)
print("---------------------------------------------------")

print("Practical Exercise")
python = 75
sql = 80
print(python >= 50 and sql >= 50)
maths = 35
science = 85
print(maths >= 80 or science >= 80)
is_absent = False
print(not is_absent)
age = 22
education = True
print(age >= 18 and education == True)
print("--------------------------------")

print("Conditional Statements")
print("if")
marks = 90
if marks >=75:
    print("Passed")

age = 22
if age>=18:
    print("Eligible to Vote")

print('if-else')
marks = 30
if marks >= 45:
    print("Student Passed")
else:
    print("Student Failed")
print("------------------------")

print("Practical Exercise")
print("Pass or Fail")
marks = 35
if marks >= 40:
    print("Pass")
else:
    print("Fail")
print()

print("Voting Eligibility")
age = 16
if age >=18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
print()

print("Positive or Negative Number")
number = -10
if number >= 0:
    print("Positive")
else:
    print("Negative")
print("--------------------------------")

print("if-elif-else")
marks = 90
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 40:
    print("D Grade")
else:
    print("Failed")
print()

print("Student Grade Calculator")
marks = 82
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 40:
    print("D Grade")
else:
    print("Failed")
print()

print("Number Checker")
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
print("------------------")

print("Nested-if")
print("Example")
age = 22
degree = True
if age >=18:
    if degree == True:
        print("You can Apply")
    else:
        print("You need a Degree")
else:
    print("You are not Eligible")
print("--------------------------------------------------")

print("Practical Exercise")
age = 22
degree = True
if age >= 18:
    if degree == True:
        print("Eligible for Job")
    else: 
        print("Degree Required")
else:
    print("Not eligible because age is below 18.")
print()

print("ATM Withdrawal")
balance = 5000
withdraw_amount = 3000
if withdraw_amount > 0:
    if balance >= withdraw_amount:
        print("Withdrawal Successful")
    else:
        print("InSufficient Balance")
else:
    print("Invalid Amount")
print("--------------------------------------------------------------")

print("Mini-Project")
name= input("Enter Student Name: ")
math = int(input("Enter Maths marks: "))
socsci = int(input("Enter SocailStudies marks: "))
gk = int(input("Enter General Knowledge Marks: "))
total_marks = math + socsci + gk
percentage = (total_marks/300) * 100
print("Student name is: ",name)
print("Math Marks is: ", math)
print("Social Studies Marks is: ", socsci)
print("General Knowledge is: ", gk)
print("Total Marks Obtained = ", total_marks)
print("Percentage: ", percentage)
if math >= 40 and socsci >= 40 and gk >= 40:
    print("Pass")

    if percentage >= 90:
        print("A Grade")
    elif percentage >= 75:
        print("B Grade")
    elif percentage >= 60:
        print("C Grade")
    elif percentage >= 40:
        print("D Grade")
else:
    print("Failed")