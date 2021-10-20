#Lab3 Question 4
#Alan Vuong
#Description of Program: This program calculates the total pay after commission from using the total sales and advanced pay. The commission varies by the amount of sales.

# Functions
#Input data by user
def get_sales()->float:
	'''This function gets the monthly sales from the user and returns it'''
	sales = float(input("Enter the monthly sales: "))

	return sales

def get_advanced_pay()->float:
	'''This function asks the user to enter the advanced pay they received'''
	print("Enter the amount of advanced pay, or")
	print("enter 0 if no advanced pay was given.")
	advanced_pay = float(input("Advanced pay: "))

	return advanced_pay

#Processing / Calculations
def determine_comm_rate(sales: float)->float:
	'''This function returns the commission rate based on the amount of sales'''
	if sales < 10000.00:
		comm_rate = 0.10
	elif sales >= 10000.00 and sales <= 14999.99:
		comm_rate = 0.12
	elif sales >= 15000.00 and sales <= 17999.99:
		comm_rate = 0.14
	elif sales >= 18000.00 and sales <= 21999.99:
		comm_rate = 0.16
	elif sales > 21999.99:
		comm_rate = 0.18

	return comm_rate


# Main Function -- Call other functions
# This program calculates a salesperson's pay 
 
def main(): 
    # Get the amount of sales from user 
    sales = get_sales() 
 
    # Get the amount of advanced pay from user. 
    advanced_pay = get_advanced_pay() 
 
    # Determine the commission rate. 
    comm_rate = determine_comm_rate(sales) 
 
    # Calculate the pay. 
    pay = sales * comm_rate - advanced_pay 
 
    # Display the amount of pay. 
    print('The pay is $', format(pay, ',.2f'), sep='') 
 
    # Determine whether the pay is negative. 
    if pay < 0: 
        print('The salesperson must reimburse') 
        print('the company.') 


if __name__ == "__main__":
	main()

## Test Run 1 for Q4
# Enter the monthly sales: 14550.00
# Enter the amount of advanced pay, or 
# enter 0 if no advanced pay was given.
# Advanced pay: 1000.00
# The pay is $746.00

## Test Run 2 for Q4
# Enter the monthly sales: 9500
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay: 0
# The pay is $950.00

## Test Run 3 for Q4
# Enter the monthly sales: 12000.00
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay: 2000.00
# The pay is $-560.00
# The salesperson must reimburse
# the company.