#Lab2 Question 7
#Alan Vuong
#Description of Program: This program accepts user input wholesale prices to calulate retail prices, where the markup is 2.5 times the wholesale price. Validation will be used to check if the inputted value is out of range and displays a message to let the user know when an error is encountered. Validation: Wholesale price !< 0

#Initialize variables
add_item = 'Y'

while add_item == 'Y' or add_item == 'y':
	#Input data by user
	wholesale_price = float(input("Enter the item's wholesale cost: "))

	while wholesale_price < 0:			# Validation check for user input
		print("ERROR: the cost cannot be negative")
		wholesale_price = float(input("Enter the correct wholesale cost: "))

	#Constants
	MARKUP = 2.5

	#Processing
	retail_price = wholesale_price * MARKUP

	#User Output
	print("Retail price is $" + '{:.2f}'.format(retail_price))

	add_item = input("Do you have another item? (Enter y for yes): ")



##Test Run 1 for Q7
## Enter the item's wholesale cost: -.50
## ERROR: the cost cannot be negative
## Enter the correct wholesale cost: .50
## Retail price is $1.25
## Do you have another item? (Enter y for yes): n

## Test Run 2 for Q7
## Enter the item's wholesale cost: .75
## Retail price is $1.88
## Do you have another item? (Enter y for yes): Y
## Enter the item's wholesale cost: .50
## Retail price is $1.25
## Do you have another item? (Enter y for yes): n

## Test Run 3 for Q7
## Enter the item's wholesale cost: 1.50
## Retail price is $3.75
## Do you have another item? (Enter y for yes): y
## Enter the item's wholesale cost: .35
## Retail price is $0.88
## Do you have another item? (Enter y for yes): y
## Enter the item's wholesale cost: -0.1
## ERROR: the cost cannot be negative
## Enter the correct wholesale cost: 0.42
## Retail price is $1.05
## Do you have another item? (Enter y for yes): n
