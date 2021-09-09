#Alan Vuong
#Student ID: 1166772
#Homework 1 Program Set 1
#This program computes the monthly payment and total payment, when given the
#annual interest rate, the number of years, and the loan amount.

#data/input
annualInterestRate = float(input("Enter annual interest rate, (e.g., 7.25): "))
numYears = int(input("Enter number of years as integer, (e.g., 5): "))
loanAmount = float(input("Enter loan amount, (e.g., 120000.95): "))

#Processing/Calculations
monthlyInterestRate = annualInterestRate / 1200
monthlyPayment = (loanAmount * monthlyInterestRate) / (1-1 / ( (1 + monthlyInterestRate) ** (numYears * 12)))
totalPayment = monthlyPayment * numYears * 12

# formatting decimal numbers with 2 decimal points and commas
monthlyPayment = format(monthlyPayment, ',.2f')
totalPayment = format(totalPayment, ',.2f')

#Output
print("\nThe monthly payment is " + str(monthlyPayment))		# typecasting float to string
print("The total payment is " + str(totalPayment))			# type casting float to string

#ask user to stop program
input('\nPress enter key to quit')

## Output (5 Test Runs)
## Test Run 1
## Enter annual interest rate, (e.g., 7.25): 4.5
## Enter number of years as integer, (e.g., 5): 30
## Enter loan amount, (e.g., 120000.95): 350000.50
##
## The monthly payment is 1,773.40
## The total payment is 638,424.40
##
## Press enter key to quit
##

## Test Run 2
## Enter annual interest rate, (e.g., 7.25): 3.0
## Enter number of years as integer, (e.g., 5): 20
## Enter loan amount, (e.g., 120000.95): 400000.10
## 
## The monthly payment is 2,218.39
## The total payment is 532,413.83
##
## Press enter key to quit
##

## Test Run 3
## Enter annual interest rate, (e.g., 7.25): 5.2       
## Enter number of years as integer, (e.g., 5): 40        
## Enter loan amount, (e.g., 120000.95): 100000.65 
## 
## The monthly payment is 495.52
## The total payment is 237,849.81
##
## Press enter key to quit
##

## Test Run 4
## Enter annual interest rate, (e.g., 7.25): 2.2
## Enter number of years as integer, (e.g., 5): 15
## Enter loan amount, (e.g., 120000.95): 30000.85
## 
## The monthly payment is 195.83
## The total payment is 35,250.00
##
## Press enter key to quit
##

## Test Run 5
## Enter annual interest rate, (e.g., 7.25): 4.2
## Enter number of years as integer, (e.g., 5): 10
## Enter loan amount, (e.g., 120000.95): 4000.00 
## 
## The monthly payment is 40.88
## The total payment is 4,905.52
## 
## Press enter key to quit
##