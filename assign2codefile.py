#QUESTION 1 :

print("The solution for QUESTION:1 is: \n")
input_str = "Python is a case sensitive language"
# a) to find the length of the string
print("a) The length of the given string is :", len(input_str))
# b) to reverse the order of the string
reverse_str = input_str[::-1]
print("b) The reversed order string string is: ", reverse_str)
# c) using slice function to store "a case sensitive" in new string
sliced_str = input_str[10:26]
print("c) The new sliced string is: ", sliced_str )
# d) replace "a case sensitive" with "object oriented"
replace_str = input_str.replace("a case sensitive","object oriented")
print("d) The replaced string is: ", replace_str)
# e) finding index of substring "a"
sub_str = "a"
indx = input_str.find(sub_str)
if(indx==-1):
    print("e) The substring a is not found in the string." )
else:
    print("e) The index of the substring a here is:", indx)
# f) removing white spaces from the given string
no_white_space_str = input_str.replace(" ", "")
print("f) The input string without any white spaces is: ", no_white_space_str)
print(" ")

# QUESTION 2 :

print("The solution for QUESTION:2 is: \n")
#inputs
name = input("Enter your name : ")
sid = int(input("Enter your SID : "))
dept_name = input("Enter the name of your department : ").upper()
cgpa=float(input("Enter your CGPA : "))
#output
print("\nHey, \033[1m%s\033[0m Here!\nMy SID is \033[1m%d\033[0m\nI am from \033[1m%s\033[0m department and my CGPA is \033[1m%0.1f\033[0m\n" % (name, sid, dept_name, cgpa))
print(" ")

# QUESTION 3 :

print("\nThe solution of Question 3 is :\n")
a=56
b=10
print("a.\ta & b = %d" % (a & b))
print("b.\ta | b = %d" % (a | b))
print("c.\ta ^ b = %d" % (a ^ b))
print("d.\tLeft shift both a and b with 2 bits : a = %d, b = %d" % (a << 2,b << 2))
print("e.\tRight shift a with 2 bits and b with 4 bits : a = %d, b = %d\n" % (a >> 2,b >> 4))
print(" ")

# QUESTION 4 :

print("\nThe solution of Question 4 is :\n")
# Entering the input  numbers
first_no = int(input("Enter the first number: "))
second_no = int(input("Enter the second number: "))
third_no = int(input("Enter the third number: "))
if first_no >= second_no:
    if first_no >= third_no:
        print("The greatest number is %s\n" % first_no)
    else:
        print("The greatest number is %s\n" % third_no)
else:
    if second_no >= third_no:
        print("The greatest number is %s\n" % second_no)
    else:
        print("The greatest number is %s\n" % third_no)
print(" ")

# QUESTION 5 :

print("The solution for QUESTION:5 is: \n")
inp_str = input("Enter your string: ")
if ("name" in inp_str):
    print("YES\n")
else:
    print("NO\n")
print(" ")

# QUESTION 6 :

print("The solution for QUESTION:6 is: \n")
side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))

sidelist = [ side1,side2,side3]
sidelist.sort()


if (sidelist[2]>sidelist[0]+sidelist[1]):
  print("Yes, a triangle can be formed by these sides. ")
else:
    print("NO, a triangle cant be formed by these 3 lengths.")






