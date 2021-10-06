#Lab2 Question 4
#Alan Vuong
#Description of Program: This program accepts a single character as user input and checks whether it is a number(0-9) or a character. If it is a character, determine whether it is uppercase or lowercase. If it is a number, display "A number was entered".

#Input data by user
user_input = input("Enter any character: ")

#Constants
UPPER_FIRST = 'A'
UPPER_LAST = 'Z'
LOWER_FIRST = 'a'
LOWER_LAST = 'z'

#Processing
if user_input >= UPPER_FIRST and user_input <= UPPER_LAST:
    print("Uppercase character was entered")
elif user_input >= LOWER_FIRST and user_input <= LOWER_LAST:
    print("Lowercase character was entered")
else:
    print("A number was entered")

## Test Run 1 for Q4
## Enter any character: C
## Uppercase character was entered
## 
## Test Run 2 for Q4
## Enter any character: b
## Lowercase character was entered
## 
## Test Run 3 for Q4
## Enter any character: 2 
## A number was entered