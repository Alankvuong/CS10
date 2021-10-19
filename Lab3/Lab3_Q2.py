#Lab3 Question 2
#Alan Vuong
#Description of Program: This program will calculate the interest of a prinipal amount within a function. The function will take in 3 parameters: rate(0.01), period(10), principal(10000.00) and will print the calculated interest.

# Functions
def show_interest(rate: float, period: int, principal: float) -> None:
	'''Calculates the interest from a given principal, rate, and period'''
	interest = principal * rate * period
	print("The simple interest will be $" + '{:,.2f}'.format(interest))


# Main Function -- Call other functions
def main():
	show_interest(rate = 0.01, period = 10, principal = 10000.00)
	
#Input data by user
	# None
#Processing / Calculations
	# None
#User Output
	# Above within function


if __name__ == "__main__":
	main()

## Test Run 1 for Q2
# The simple interest will be $1,000.00

## Test Run 2 for Q1
# The simple interest will be $1,000.00

## Test Run 3 for Q1
# The simple interest will be $1,000.00