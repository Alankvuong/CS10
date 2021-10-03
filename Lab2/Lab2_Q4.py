#Lab2 Question 4
#Alan Vuong
#Description of Program: This program accepts a single character as user input and checks whether it is a number(0-9) or a character. If it is a character, determine whether it is uppercase or lowercase. If it is a number, display "A number was entered".

#Input data by user
user_input = input("Enter any character: ")

#Calculations
if user_input.isdigit() == True:
    print("A number was entered")
elif user_input.isupper() == True:
    print("Uppercase character was entered")
else:
    print("Lowercase character was entered")

##Test Run 1 for Q4
