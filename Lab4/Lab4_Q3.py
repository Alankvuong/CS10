#Lab 4 Question 3
#Alan Vuong
#Description of Program: Create a program that generates a tuple containing both positive and negative numbers. Make a new tuple that only has positive values and sort it in descending order.

# Functions
def makeTuple()->tuple:
	'''Function gets 10 values and puts it into a tuple'''

	userString = input("Enter the values in a tuple: ")
	
	string_numbersList = userString.split(',')				# Splits the string of numbers into a list

	string_numbersList_length = len(string_numbersList)		# Gets range of list for loop
	int_numbersList = []
	
	# Loops through list and appends string->int to new list
	for i in range(string_numbersList_length):
		int_numbersList.append(int(string_numbersList[i]))

	return tuple(int_numbersList)

def makePositive(numbersTuple: tuple)->tuple:
	'''Function creates a new tuple with positive numbers in descending only from tuple created in makeTuple()'''

	numbersTupleLength = len(numbersTuple)
	
	positiveList = []
	for i in range(numbersTupleLength):
		if(numbersTuple[i] > 0):
			positiveList.append(numbersTuple[i])

	positiveList.sort(reverse=True)
	
	positiveTuple = tuple(positiveList)

	return positiveTuple

# Main Function -- Call other functions
def main():
	numbersTuple = makeTuple()
	positiveTuple = makePositive(numbersTuple)

	print("\nOriginal Tuple :", numbersTuple)
	print("New Tuple with Positive numbers :", positiveTuple)

	

#Input data by user
	# None
#Processing / Calculations
	# None
#User Output
	# Above within function


if __name__ == "__main__":
	main()

## Test Run 1 for Q3
# Enter the values in a tuple: -10, 1, 2, -9, 3, 4, -8, 5, 6, -7

# Original Tuple : (-10, 1, 2, -9, 3, 4, -8, 5, 6, -7)
# New Tuple with Positive numbers : (6, 5, 4, 3, 2, 1)
