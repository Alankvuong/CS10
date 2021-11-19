#Lab 4 Question 2
#Alan Vuong
#Description of Program: Create a program to remove all duplicates from a list.

# Functions
def createList()->list:
	'''Create a list from user inptuted values(10 integers)'''
	numList = []

	i = 0
	while i < 10:
		userInput = int(input("Enter a number to be added to a list: "))		#Input data by user
		numList.append(userInput)
		i += 1

	return numList


def removeDuplicates(numList:list)->list:
	'''Function will remove duplicate values from list'''
	
	numList.sort()
	index = 0
	while index < len(numList):
		currNum = numList[index]
		index2 = index + 1
		while index2 < len(numList):
			nextNum = numList[index2]
			if currNum == nextNum:
				numList.remove(currNum)
			index2 += 1
		index += 1

	return numList


# Main Function -- Call other functions
def main():
	numList = createList()
	newNumList = removeDuplicates(numList)

	#User Output
	print("\nOriginal List :", numList)
	print("List after removing duplicates :", newNumList)


if __name__ == "__main__":
	main()

## Test Run 1 for Q2
# Enter a number to be added to a list: 1
# Enter a number to be added to a list: 2
# Enter a number to be added to a list: 3
# Enter a number to be added to a list: 4
# Enter a number to be added to a list: 5
# Enter a number to be added to a list: 6
# Enter a number to be added to a list: 7
# Enter a number to be added to a list: 6
# Enter a number to be added to a list: 5
# Enter a number to be added to a list: 4
# 
# Original List : [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]
# List after removing duplicates : [1, 2, 3, 4, 5, 6, 7]