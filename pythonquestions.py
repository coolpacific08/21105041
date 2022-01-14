#PYTHON ASSIGNMENT-1

# QUESTION 1
print("This is output of question 1 :")

num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))

average = (num1+num2+num3)/3
print("Average is : ",average)

#QUESTION 2
print("")
print("This is output of question 2 :")

#All amount is calculated in dollars
standard_deduction = 10000
# deduction per head
dependent_deduction = 3000
gross_income = int(input(" What is your gross income ? "))
dependents = int(input(" How many dependents do you have ? "))

taxable_income = gross_income-standard_deduction-(dependent_deduction*dependents)
tax = float((taxable_income)*(20/100)) # Tax rate is 20%
print("Your income tax is : ",tax)

#QUESTION 3
print("")
print("This is output of question 3 :")

SID = int(input("Enter SID: "))
name = str(input("What is your name ? "))
gender = str(input ("Enter gender: "))
course_name = str(input("Enter course name: "))
CGPA = float(input("Enter your CGPA: "))
student = [SID, name, gender, course_name, CGPA]

print(student)


#QUESTION 4
print("")
print("This is output of question 4 :")
marks1 = int(input("Marks of student 1 : "))
marks2 = int(input("Marks of student 2 : "))
marks3 = int(input("Marks of student 3 : "))
marks4 = int(input("Marks of student 4 : "))
marks5 = int(input("Marks of student 5 : "))

list = [marks1,marks2,marks3,marks4,marks5] #before sorting
print(list)
list.sort()
print('list after sorting', list) #after sorting

#QUSETION 5
print("")
print("This is output of question 5 :")
colour = ['Red','Green','White','Black','Pink','Yellow']
colour.remove('Black')
print("Part a : ",colour)

colour = ['Red','Green','White','Black','Pink','Yellow']
colour[3:5] = ['Purple'] # Replacing Black and Pink with Purple
print("Part b : ",colour)















