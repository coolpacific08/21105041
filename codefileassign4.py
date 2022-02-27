print("***********************************ASSIGNMENT 4***********************************")
print("")
print("This is solution of Question 1:")

# Recursive Python function to solve the tower of hanoi
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)

# Calling Function Tower of Hanoi
n = 3
TowerOfHanoi(n,'A','B','C')
# A, B, C are the name of rods
print("")

#  *******************************************************************************************

print("This is solution of Question 2:")
n = int(input("Enter the number of rows in Pascal's triangle: "))

print("Using iterations.")
for i in range(1, n + 1):
    for j in range(0, n - i):
        print(' ', end='')

     # first element is always 1
    C = 1
    for j in range(1, i + 1):
        # first value in a line is always 1
        print(C,'', end='')

       # using Binomial Coefficient
        C = C * (i - j) // j
    print("")

print("Using recursions.")
def pascal(n, originaln=n):
    if n == 0:
        return

    pascal(n - 1, originaln)

    # printing the spaces
    print('  ' * (originaln - n), end='')

    # first number is always 1
    entry = 1
    for i in range(1, n + 1):
        print(entry, end='   ')

        # using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)
print("")

# ******************************************************************************
print("This is solution of Question 3:")
def quot_remain(a,b):
    c = a % b
    d = a // b
    print(f"the remainder is {c} and quotient is {d}.\n")

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = a % b
d = a // b
quot_remain(a,b)

print("part a)")
callability = callable(quot_remain)
if callability == True:
    print("Function is callable.")
else:
    print("Function is not callable.")
print()

print("part b)")
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
print()

print("part b)")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

# ******************************************************************************
print("This is solution of Question 4:")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Data deleted")

# creating object
student1 = Student("Prashant Kumar Singh", 21105041)
print("Object created")

# printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

# deleting object
del student1
print("")

#***************************************************************************************
print("This is solution of Question 5:")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name} record deleted")

# creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# part a, updating salary
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

# part b, deleting a record
print("b. ", end='')
del employee3
print(" ")

#*******************************************************************************************
print("This is solution of Question 6:")

# Uttered word from first friend
inp_word = input("Enter any word that comes to your mind.\n")
# Word guessed by the second friend
guess_word = input("Write a new word with the same letters.\n")

def letter_in_word(word):
    count = dict()
    letter = tuple(word)
    for i in letter:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

# verifying the letters of words given by the two friends
if letter_in_word(inp_word) != letter_in_word(guess_word):
    print("The letters aren't exact, friendship is fake!!")
else:
    print("Congratulations, You have a good friendship.")






