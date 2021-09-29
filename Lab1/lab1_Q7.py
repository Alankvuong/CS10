#Lab 1 Question 7
#Alan Vuong
#Description: This program asks the user to enter a 4 digit number and displays the number in reverse order 

#input data by user
num = int(input("Enter an integer: "))

# Calculations (obtaining digits)
lastDigit = num % 10
num //= 10
thirdDigit = num % 10
num //= 10
secondDigit = num % 10
num //= 10
firstDigit = num % 10
num //= 10

# Print the 4 digits on separate lines
print(lastDigit)
print(thirdDigit)
print(secondDigit)
print(firstDigit)

#Promps user to exit
input('\n\nPress the enter key to quit\n\n')

##Test run 1 for Q7
##Enter an integer: 3125
##5
##2
##1
##3
##
##
##Press the enter key to quit
##
##
## Test run 2 for Q7
##Enter an integer: 1234
##4
##3
##2
##1
##
##
##Press the enter key to quit
##
##
## Test run 3 for Q7
##Enter an integer: 8423
##3
##2
##4
##8
##
##
##Press the enter key to quit
##
##