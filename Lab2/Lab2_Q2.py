#Lab2 Question 2
#Alan Vuong
#Description of Program: This program finds whether or not the user inputted number is even or odd. 

#Input data by user
num_input = int(input("Enter any number: "))
odd_or_even = bool

#Calculations
if(num_input % 2 == 0):
    odd_or_even = True
else:
    odd_or_even = False

#User output
if(odd_or_even == True):
    print(str(num_input) + " is even")
else:
    print(str(num_input) + " is odd")

## Test Run 1 for Q2
## Enter any number: 125
## 125 is odd
## 
## Test Run 2 for Q2
## Enter any number: 12
## 12 is even
## 
## Test Run 3 for Q2
## Enter any number: 891
## 891 is odd