#Lab 4 Question 4
#Alan Vuong
#Description of Program: Write a program to read a sequence of string values and prints them, and marks the largest number. 

# Functions
def readValues()->list:
	'''Ask user to enter in any amount of numbers until they enter 'Q' '''
	numList = []

	userInput = input("Please enter values, Q to quit:\n")

	while userInput != 'Q':
		numList.append(userInput)
		userInput = input()
	
	return numList

def findLargest(numList: list)->float:
	'''Receives the list as a parameter and returns the largest number from the list'''

	numList_int = []
	numList_length = len(numList)

	for i in range(numList_length):
		numList_int.append(float(numList[i]))
				
	largestNum = 0
	numList_int_length = len(numList_int)
	for i in range(numList_int_length):
		if numList_int[i] > largestNum:
			largestNum = numList_int[i]

	return largestNum

def display(numList: list, largestNum: float)->None:
	'''This displays the list and the largest number in the list'''

	print("\nHere are the numnbers in the list")

	numList_length = len(numList)

	for i in range(numList_length):
		string_to_int = float(numList[i])
		if string_to_int == largestNum:
			print(numList[i] + " <== this is the largest number")
		else:
			print(numList[i])

# Main Function -- Call other functions
def main():
	numList = readValues()
	largestNum = findLargest(numList)
	display(numList, largestNum)
	

#Input data by user
	# Within function readValues()
#Processing / Calculations
	# Within Functions
#User Output
	# Above within function


if __name__ == "__main__":
	main()

## Test Run 1 for Q4
# Please enter values, Q to quit:
# 34
# 56.7
# 4
# 9
# 76.9
# 55.4
# Q

# Here are the numnbers in the list
# 34
# 56.7
# 4
# 9
# 76.9 <== this is the largest number
# 55.4
