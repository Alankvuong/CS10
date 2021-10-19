#Lab3 Question 1
#Alan Vuong
#Description of Program: This program has a main function that calls two other functions: texas() and california(). Each function has a local variable named birds that is isolated to the function scope, which will be printed respectively.

# Functions
def texas() -> None:
	'''Prints the number of birds in Texas'''

	birds = 5000
	print("Texas has " + str(birds) + " birds.")

def california() -> None:
	'''Prints the number of birds in California'''

	birds = 8000
	print("California has " + str(birds) + " birds.")

# Main Function -- Call other functions
def main():
	texas()
	california()
	
#Input data by user
	# None
#Processing / Calculations
	# None
#User Output
	# Above within function


if __name__ == "__main__":
	main()

## Test Run 1 for Q1
# Texas has 5000 birds.
# California has 8000 birds.

## Test Run 2 for Q1
# Texas has 5000 birds.
# California has 8000 birds.

## Test Run 3 for Q1
# Texas has 5000 birds.
# California has 8000 birds.