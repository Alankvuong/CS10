#Lab2 Question 4
#Alan Vuong
#Description of Program: This program accepts a single character as user input and checks whether it is a number(0-9) or a character. If it is a character, determine whether it is uppercase or lowercase. If it is a number, display "A number was entered".

#Input data by user
user_input = input("Enter any character: ")

#Constants
upperchar_first = 'A'
upperchar_last = 'Z'
lowerchar_first = 'a'
lowerchar_last = 'z'

#Processing
if user_input >= upperchar_first and user_input <= upperchar_last:
    print("Uppercase character was entered")
elif user_input >= lowerchar_first and user_input <= lowerchar_last:
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