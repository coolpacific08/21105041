
# QUESTION 1 ;

print("This is solution of question no 1: ")
str_inp = input("Enter the string:\n")   # Taking input from user
str_inp = str_inp.lower()                # Converting input string so that every character/word is lower case.

if " " not in str_inp:                   # To check if the string is a single word or a sentence.
    print("You have entered single word." )
    char = tuple(str_inp)                # Creating a tuple of the characters of the single string.
    dict_of_char = dict()
    for item in char:
        if item not in dict_of_char:     # First occurrence of a character.
            dict_of_char[item] = 1
        else:
            dict_of_char[item]+=1        # When character is repeated in string.
    print("The no of occurances of each character in given single string is:\n ")
    print("CHARACTER-NO OF OCCURANCES \n")
    for (key, value) in sorted(dict_of_char.items()):
        print(key,"-",value)

else:
    print("You have entered a sentence string.")
    words = str_inp.split()              # Making a list of words of the string.
    dict_of_words = dict()
    for elements in words:
        if elements not in dict_of_words:   # First occurrence of word in string.
            dict_of_words[elements] = 1
        else:                               # When word is repeated in the string.
            dict_of_words[elements] += 1
    print("The no of occurances of each word in given sentence string is:\n ")
    print("WORD-NO OF OCCURANCES \n")
    for (k, v) in sorted(dict_of_words.items()):
        print(k,"-",v)
print("")

#****************************************************************************************************
# QUESTION 2 :

print("This is solution of question no 2: ")
day = int(input('Please enter Day- '))
month = int(input('Please enter Month- '))
year = int(input('Please enter Year- '))

# Removing all the invalid cases
if day > 30 and month in {2, 4, 6, 9, 11}:
    condition = False
elif day > 31 and month in {1, 3, 5, 7, 8, 10, 12}:
    condition = False
elif (day == 29 or day == 30) and month == 2 and year % 4 != 0:
    condition = False
elif day == 30 and month == 2 and year % 4 == 0:
    condition = False
else:
    condition = True

# After checking the condition, following if-else statement is executed
if condition:
    # checking and changing for new year
    if day == 31 and month == 12:
        n_year = year + 1
    else:
        n_year = year
    if month == 12 and day == 31:
        n_month = 1
    else:
        n_month = month
    # changing dates
    # checking for months with 31 days
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day == 31:
            next_day = 1
            if month != 12:
                n_month = month + 1
            else:
                n_month = 1
        else:
            next_day = day + 1
    # checking for the month of february
    elif month == 2:
        if year % 4 == 0:
            if day == 29:
                next_day = 1
                n_month = 3
            else:
                next_day = day + 1
        else:
            if day == 28:
                next_day = 1
                n_month = 3
            else:
                next_day = day + 1

    # covering all the remaining cases
    else:
        if day == 30:
            next_day = 1
            n_month = month + 1
        else:
            next_day = day + 1
    # printing the calculations
    print(f"Next Date is: {next_day}/{n_month}/{n_year}")
else:
    # gives a warning and ends the program
    print("That's not a valid date")
print(" ")

#**********************************************************************************************
# QUESTION 3:

print("This is solution of question no 3: ")
user_list = list()
# Asking the user to clarify the size of his/her list.
list_element_no = int(input("Enter the length of your list: "))
for i in range (1,list_element_no+1):
    # Asking user for the inputs for the list.
    elements = int(input("Enter the numbers: "))
    user_list.append(elements)   # Adding the elements given by user to a  empty list.
print(user_list)                 # This is the list given by user.

mod_list1 = list()               #  empty list for later use.
mod_list2 = list()               #  empty list for later use.
for items in user_list:
    mod_list1.append(items)      # Adding the items of earlier made list to new empty list.
    mod_list2.append(items**2)   # Adding the square of the items of earlier made list to new empty list.

# Finalizing the list by joining last two lists using zip function.
final_list = list(zip(mod_list1,mod_list2))
print("The final output list is: ", final_list)
print("")

#***********************************************************************************************
# Question 4:

print("This is solution of question no 4: ")
grade_input = int(input("Enter your grade point: "))
if grade_input not in range (4,11):
    print("ERROR!, Enter a valid grade point. ")
else:
    dict1 = {4:{"letter grade":"D","Performance":"Poor"},5:{"letter grade":"C","Performance":"Below Average"},
             6:{"letter grade":"C+","Performance":"Average"},7:{"letter grade":"B","Performance":"Good"},
             8:{"letter grade":"B+","Performance":"Very Good"},9:{"letter grade":"A","Performance":"Excellent"},
             10:{"letter grade":"A+","Performance":"Outstanding"}}

    print("The entered grade input is: ",grade_input)
    print("Your grade is ",dict1[grade_input]["letter grade"]," and ",dict1[grade_input]["Performance"]," performance")
print("")

#************************************************************************************************
# QUESTION 5:

print("This is solution of question no 5: ")

str = "ABCDEFGHIJK"
j = 0
while len(str) - j*2 >= 1:
    print(" "*j + str[0 : len(str) - j*2])
    j += 1
print("")

#************************************************************************************************
# QUESTION 6:

print("This is solution of question no 6: ")
student_data = dict()
while True:
    name = input("Enter the name of the student: ")
    SID = input("Enter the SID : ")
    student_data[SID] = name

    while True:
        add_more = input("Do you want to add more details?\n Enter Y for yes or N for no : ")
        if add_more == "N":
            add_more = 0
            break
        elif add_more == "Y":
            more_data = 1
            break
        else:
            print("Enter Y or N only.")
            continue
    if add_more == 0:
        break
# PART A:
print("part(a): ")
for key in student_data:
    print("The name  of student is ",student_data[key],"and the student's sid is ",key)
print("")

# PART B:
print("part(b): sorting using names")
sort_name_data = dict()
for sorted_value in sorted(student_data.values()):
    for key,value in student_data.items():
        if value == sorted_value:
           sort_name_data[key] = value
for key in sort_name_data:
    print("The name  of student is ",sort_name_data[key],"and the student's sid is ",key)
print("")

# PART C:
print("part(c): sorting using SID")
sort_SID_data = dict()
for sorted_key in sorted(student_data):
    for key,value in student_data.items():
        if key == sorted_key:
            sort_SID_data[key] = value
for key in sort_SID_data:
    print("The name  of student is ", sort_SID_data[key], "and the student's sid is ", key)
print("")

# PART D:
print("part(d): ")
while True:
    entered_SID = input("Enter the SID of student whose detail is needed-")
    if entered_SID in student_data:
        print("The name of the student: ",student_data[entered_SID])
        break
    else:
        print("Student is not found in college data, please check for error")
        continue
print(" ")

#**************************************************************************************
# QUESTION 7 :

print("This is solution of question no 7: ")
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#using the formula of the sum of previous two terms is equal to the present term.
a_n1=1
a_n2=0
n=0
#initializing sum with first two terms
sum=a_n1+a_n2

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {number} terms")
print(a_n2)
print(a_n1)

#Printing the remaining fibonnaci terms
while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number
#printing the program end prompt
print(f"Average of total {number} terms of sequence is {average}")
print(" ")

#*********************************************************************************************
# QUESTION 8:

print("This is solution of question no 8: ")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)






