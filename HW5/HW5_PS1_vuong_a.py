#Alan Vuong
#Student ID: 1166772
#Homework 5 Program Set 1
# This program will use class methods, setters, and getters to calculate the loan, monthly payment, and total payment for a loan.

class Loan:
	#Constructor for class: allows for the program to pass data from calling the object
	def __init__(self, interest_rate= 2.5, years = 1, loan_amount =  1000, name = ""):
		self.__yearly_interest_rate = interest_rate
		self.__years = years
		self.__loan_amount = loan_amount
		self.__name = name

	## Getters: Retrieves the data 
	def getInterestRate(self) -> float:
		"""Returns the yearly interest rate"""
		return self.__yearly_interest_rate

	def getYears(self) -> float:
		"""Returns the amount of time for loan"""
		return self.__years

	def getLoanAmount(self) ->float:
		"""Returns the loan amount"""
		return self.__loan_amount
	
	def getName(self) ->str:
		"""Returns the borrower's name"""
		return self.__name

	## Setters: Sets new data
	def setInterestRate(self, newInterestRate: float)->float:
		"""Sets a new interest rate"""
		self.__yearly_interest_rate = newInterestRate

	def setYears(self, newYears:float)->float:
		"""Sets the new number of years for loan"""
		self.__years = newYears
	
	def setLoanAmount(self, newLoanAmount: float)->float:
		"""Sets a new amount for the loan"""
		self.__loan_amount = newLoanAmount

	def setName(self, newName: str)->str:
		"""Sets a new name"""
		self.__name = newName


	## Class Methods
	def getMonthlyPayment(self) -> float:
		"""Method calculates and returns the monthly payment needed to borrow the loan"""
		monthly_interest_rate = self.__yearly_interest_rate / 1200
		monthlyPayment = (self.__loan_amount * monthly_interest_rate) / (1-(1/(1 + monthly_interest_rate) ** (self.__years * 12)))

		return monthlyPayment

	def getTotalPayment(self) -> float:
		"""Method calculates the total payment that the borrower needs to pay for the loan"""
		monthlyPayment = self.getMonthlyPayment()

		totalPayment = monthlyPayment * self.__years * 12

		return totalPayment


def main():
	# User input for interest rate, years, loan amount, and borrower's name
	yearlyInterestRate = float(input("Enter yearly interest rate: "))
	years = int(input("Enter number of years as an integer: "))
	loanAmount = float(input("Enter loan amount: "))
	name = (input("Enter a borrower's name: "))

	# Create a loan object from the user input above
	newLoan = Loan(yearlyInterestRate, years, loanAmount, name)

	# Outputs the corresponding details by calling the object's methods
	print("The loan is for " + newLoan.getName())
	print("The monthly payment is", '{0:,.2f}'.format(newLoan.getMonthlyPayment()))
	print("The total payment is",'{0:,.2f}'.format(newLoan.getTotalPayment()))

	loopControl = 'Y'

	# While loop to keep program running if user wants to enter a new loan
	while(loopControl == 'y' or loopControl == 'Y'):
		loopControl = input("\nDo you want to change the loan amount? Y for yes or enter to quit ")

		# if user enters yes
		if loopControl == 'y' or loopControl == 'Y':
			loanAmount = float(input("Enter new loan amount "))
			newLoan.setLoanAmount(loanAmount)

			print("The loan is for " + newLoan.getName())
			print("The monthly payment is", '{0:,.2f}'.format(newLoan.getMonthlyPayment()))
			print("The total payment is",'{0:,.2f}'.format(newLoan.getTotalPayment()))


if __name__ == "__main__":
    main()



## Test Outputs (5 Test Runs)
## Test Run 1
# Enter yearly interest rate: 2.5
# Enter number of years as an integer: 5
# Enter loan amount: 1000.00
# Enter a borrower's name: John Jones
# The loan is for John Jones
# The monthly payment is 17.75
# The total payment is 1,064.84

# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount 5000
# The loan is for John Jones
# The monthly payment is 88.74
# The total payment is 5,324.21

# Do you want to change the loan amount? Y for yes or enter to quit

## Test Run 2
# Enter yearly interest rate: 3.2
# Enter number of years as an integer: 6
# Enter loan amount: 1200.00
# Enter a borrower's name: Adam Apple
# The loan is for Adam Apple
# The monthly payment is 18.34
# The total payment is 1,320.48

# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount 800 
# The loan is for Adam Apple
# The monthly payment is 12.23
# The total payment is 880.32

# Do you want to change the loan amount? Y for yes or enter to quit

## Test Run 3
# Enter yearly interest rate: 1.2         
# Enter number of years as an integer: 8   
# Enter loan amount: 8000.00
# Enter a borrower's name: Ash Ketchum
# The loan is for Ash Ketchum
# The monthly payment is 87.44
# The total payment is 8,394.14

# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount 4200 
# The loan is for Ash Ketchum
# The monthly payment is 45.91
# The total payment is 4,406.92

# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount 1800
# The loan is for Ash Ketchum
# The monthly payment is 19.67
# The total payment is 1,888.68

# Do you want to change the loan amount? Y for yes or enter to quit

## Test Run 4
# Enter yearly interest rate: 2.2  
# Enter number of years as an integer: 2 
# Enter loan amount: 5500.00
# Enter a borrower's name: Nemo Clownfish
# The loan is for Nemo Clownfish
# The monthly payment is 234.46
# The total payment is 5,626.93

# Do you want to change the loan amount? Y for yes or enter to quit

## Test Run 5
# Enter yearly interest rate: 0.8     
# Enter number of years as an integer: 2
# Enter loan amount: 4444.50
# Enter a borrower's name: Pooh Bear
# The loan is for Pooh Bear
# The monthly payment is 186.73
# The total payment is 4,481.63

# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount 5000.25
# The loan is for Pooh Bear
# The monthly payment is 210.08
# The total payment is 5,042.03

# Do you want to change the loan amount? Y for yes or enter to quit