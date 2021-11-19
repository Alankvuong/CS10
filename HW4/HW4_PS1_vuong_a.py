#Alan Vuong
#Student ID: 1166772
#Homework 4 Program Set 1
# This program will use functions to carry out tasks(a-j) specified in the directions using list methods for a list of integers.

# Define constant variables.
# ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		    	#this is test run 1
# ONE_TEN =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]   #this is test run 2, comment
ONE_TEN = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]           #this is test run 3,
                                                        #run test run 1 first, then
                                                        #comment out test run 1 and 
                                                        #uncomment to run test run 2 
                                                        #and so forth for test run 3 


def main() :
	print("The original data for all functions is: ", ONE_TEN)

	#a. Demonstrate swapping the first and last element.
	data = list(ONE_TEN)
	swapFirstLast(data)         #call this function      
	print("After swapping first and last: ", data)

	#b. Demonstrate shifting to the right.
	data = list(ONE_TEN)
	shiftRight(data)            #call this function
	print("After shifting right: ", data)

	#c. Demonstrate replacing even elements with zero.
	data = list(ONE_TEN)
	replaceEven(data)           #call this function
	print("After replacing even elements: ", data)

	#d. Demonstrate replacing values with the larger of their neighbors.
	data = list(ONE_TEN)
	replaceNeighbors(data)      #call this function
	print("After replacing with neighbors: ", data)

	#e. Demonstrate removing the middle element.
	data = list(ONE_TEN)
	removeMiddle(data)          #call this function
	print("After removing the middle element(s): ", data)

	#f. Demonstrate moving even elements to the front of the list.
	data = list(ONE_TEN)
	evenToFront(data)           #call this function
	print("After moving even elements: ", data)

	#g. Demonstrate finding the second largest value.
	print("The second largest value is: ", secondLargest(ONE_TEN))

	#h. Demonstrate testing if the list is in increasing order.
	print("The list is in increasing order: ", isIncreasing(ONE_TEN))

	#i. Demonstrate testing if the list contains adjacent duplicates.
	print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))

	#j. Demonstrate testing if the list contains duplicates.
	print("The list has duplicates: ", hasDuplicate(ONE_TEN))


#here are 2 sample functions for item a and b

def swapFirstLast(data:list)->list:
	'''Swap the first and last element in a list.''' 

	dataList_length = len(data) - 1
	firstNum = data[0]
	lastNum = data[dataList_length]

	data[0] = lastNum
	data[dataList_length] = firstNum 

	return data
   

def shiftRight(data:list)->list:
	'''Shift the elements of list to the right.'''

	lastNum = data.pop()

	data.insert(0, lastNum)

	return data


##Complete the rest of the functions from items c to j

def replaceEven(data:list)->list:
	'''Replace all even numbers with 0'''

	dataList_length = len(data)

	for i in range(dataList_length):
		if data[i] % 2 == 0:
			data[i] = 0
	
	return data


def replaceNeighbors(data:list)->list:
	'''Replaces values with the larger of its neighbor'''

	dataList_length = len(data)-1
		
	for i in range(1, dataList_length):
		if i == dataList_length:
			leftNeighbor = dataList_length[i-1]
			rightNeighbor = None
		else:
			leftNeighbor = data[i-1]
			rightNeighor = data[i+1]

		if leftNeighbor < rightNeighor:
			data[i] = rightNeighor
		elif rightNeighor < leftNeighbor:
			data[i] = leftNeighbor

	return data


def removeMiddle(data:list)->list:
	'''This removes the middle element from the list'''

	dataList_length = len(data)

	mid = dataList_length // 2
	data.pop(mid)	
	dataList_length = len(data)
	mid = dataList_length // 2
	data.pop(mid)	

	return data


def evenToFront(data:list)->list:
	'''This moves the even numbers to the front of the list'''
	dataList_length = len(data)

	evensList = []
	oddsList = []
	
	for i in range(0, dataList_length):
		if data[i] % 2 == 0:
			evensList.append(data[i])
		elif data[i] % 2 != 0:
			oddsList.append(data[i])
	
	for i in range(0, len(oddsList)):
		evensList.append(oddsList[i])

	for i in range(len(data)):
		data[i] = evensList[i]

	return data


def secondLargest(data: list)->int:
	'''This finds the second largest number in the list'''

	tempList = list(data)

	tempList.sort()

	secondLargestNum = tempList[-2]
	return secondLargestNum


def isIncreasing(data: list)->bool:
	'''Checks to see if the list is increasing throughout'''
	increasingNums = True
	i = 0 
	while (i < len(data)-1) and increasingNums != False:
		numOne = data[i]
		numTwo = data[i+1]

		if numOne < numTwo:
			increasingNums = True
		elif numOne > numTwo:
			increasingNums = False
		i += 1

	return increasingNums


def hasAdjacentDuplicate(data: list)->bool:
	'''This checks the list for adjacent duplicates'''

	adjacentDuplicate = False
	dataList_length_index = len(data)-1		# subtrcts one because lists start at 0

	for i in range(dataList_length_index):
		firstNum = data[i]
		secondNum = data[i+1]
		
		if firstNum == secondNum:
			adjacentDuplicate = True

	return adjacentDuplicate


def hasDuplicate(data: list)->bool:
	'''This checks the list for duplicates'''

	hasDuplicate = False
	listToSet = set(data)

	if len(listToSet) != len(data):
		hasDuplicate = True
	else:
		hasDuplicate = False

	return hasDuplicate


if __name__ == "__main__":
    main()



## Test Outputs (3 Test Runs)
## Test Run 1
# The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]  
# After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]   
# After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
# After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10] 
# After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]     
# The second largest value is:  9
# The list is in increasing order:  True
# The list has adjacent duplicates:  False
# The list has duplicates:  False

## Test Run 2
# The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
# After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
# After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
# After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
# After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
# After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]
# After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
# The second largest value is:  79
# The list is in increasing order:  False
# The list has adjacent duplicates:  False
# The list has duplicates:  False

## Test Run 3
# The original data for all functions is:  [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]
# After swapping first and last:  [10, 25, 25, 4, 5, 4, 7, 60, 9, 1]
# After shifting right:  [10, 1, 25, 25, 4, 5, 4, 7, 60, 9]
# After replacing even elements:  [1, 25, 25, 0, 5, 0, 7, 0, 9, 0]
# After replacing with neighbors:  [1, 25, 25, 25, 25, 25, 60, 60, 60, 10]
# After removing the middle element(s):  [1, 25, 25, 4, 7, 60, 9, 10]
# After moving even elements:  [4, 4, 60, 10, 1, 25, 25, 5, 7, 9]
# The second largest value is:  25
# The list is in increasing order:  False
# The list has adjacent duplicates:  True
# The list has duplicates:  True
