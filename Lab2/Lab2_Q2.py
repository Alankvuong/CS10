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

#User input
if(odd_or_even == True):
    print(str(num_input) + " is even")
else:
    print(str(num_input) + " is odd")

##Test Run 1 for Q2
