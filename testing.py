# TASK 1
# Declare two variables, num1 and num2, with any integer values.  Use these to calculate their sum and print  the result. Understand how variables store numerical values and perform basic arithmetic in Python.
num1=int(input('Enter the num1 for addition '))
num2=int(input('Enter the num2 for addition '))
addition_of_number=int(num1+num2)
print('The addition of',num1,'and',num2,'=',addition_of_number )

# TASK 2
# Create a variable, message, and assign it a string value. Append another string, " World!", to it and print the result.
message="Thank you "
message=message+"For coperating with us"
print(message)


# TASK 3
# Define a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun.
is_python_fun=bool(True)
print("is python fun",is_python_fun)


# TASK 4
# Create a list, fruits, with three different fruit names. Print the list and then add a new fruit to it. Print the updated list.
fruits_names=["apple","banana","orange"]
print("the fruits before updating the list",fruits_names)
fruits_names.append("Watermelon")
print("the fruits after updating the list",fruits_names)


# TASK 5
# Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values.Explore how to convert between different data types in Python.
price = 23.99
converted_price = int(price)
print("Original Price (float):", price)
print("Converted Price (int):", converted_price)


# TASK 6
# Create a dictionary, student_info, with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary.
information={"Name" :input("ENTER NAME "),
             'Age' : int(input("ENTER AGE ")),
             'Grade' :input("ENTER GRADE ")}
print("THE USER INFORMATION IS",information)


# TASK 7
# Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult").
User_age=input("Enter the age ")
Age=int(User_age)
if Age<=19:
    print("The user age  is",Age,"which mean he or she is Teenager")
else:
    print("The user age  is",Age,"which mean he or she is Adult")


# TASK 9
# Combine two strings using string concatenation, and then use string interpolation to include the length of the resulting string in a print statement.
string_1="GOOD"
string_2="PLAYER"
concatenation=string_1+string_2
print("the concatenation of two strings =",concatenation,"and","The lenght of resulting string = ",len(concatenation))


# TASK 10
# Create a tuple, days_of_week, with the names of the days. Access and print the third day of the week.
tuple_list_of_days_in_week=('Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday')
third_day_of_the_week=tuple_list_of_days_in_week[2]
print("The third day of Week is",third_day_of_the_week)