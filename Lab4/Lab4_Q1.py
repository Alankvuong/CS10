#Lab 4 Question 1
#Alan Vuong
#Description of Program: Create a program to create a list of numbers in the range of 1 to 10. Delete all the even numbers from the list and print it.

# Functions
def makeList()->list:
	'''Creates a list of numbers from 1 to 10'''

	listNum = []				# create an empty list

	for i in range(1,11):		# For loop to fill list with 1-10
		listNum.append(i)

	return listNum

def delEven(listNum: list)->list:
	'''Deletes even numbers from list'''

	for i in listNum:
		if i % 2 == 0:				# Checks if current number is even
			listNum.remove(i)
	
	return listNum

# Main Function -- Call other functions
def main():
	listNum = makeList()
	print("Original List:", listNum)

	oddOnlyList = delEven(listNum)

	print("List after deleting even numbers:", oddOnlyList)


#Input data by user
	# None
#Processing / Calculations
	# None
#User Output
	# Above within function


if __name__ == "__main__":
	main()

## Test Run 1 for Q1
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List after deleting even numbers: [1, 3, 5, 7, 9]