#Lab 4 Question 5
#Alan Vuong
#Description of Program: This program will create new sets of elements that are derived from the sets given to us. set1 = {1,2,3,4,5}, set2 = {2,4,6,8}, set3 = {1,5,9,13,17}. 

# Functions
def letterA(setOne: set, setTwo: set)->set:
	'''Creates a set of all elements that are in set1 or set2, but not both'''
	setA = setOne ^ setTwo			# Symmetric difference operator (Anything not in both sets)

	return setA

def letterB(setOne: set, setTwo: set, setThree: set)->set:
	'''Create a new set of all elements that are in only one of the three sets set1,set2, and set3.'''

	setB = setOne ^ setTwo ^ setThree			# Symmetric difference operator (Anything not in both sets)

	return setB

def letterC(setOne: set, setTwo: set, setThree: set)->set:
	'''Create a new set of all elements that are exactly two of the sets set1, set2, and set3'''

	setC = (setOne & setTwo) | (setTwo & setThree) | (setOne & setThree)

	return setC

def letterD(setOne: set)->set:
	'''Create a new set of all integer elements in the range 1 through 25 that are not in set1.'''

	tempSet = set()
	for i in range(1,26):
		tempSet.add(i)
	
	setD = tempSet - setOne

	return setD

def letterE(setOne: set, setTwo: set, setThree: set)->set:
	'''Create a new set of all integer elements in the range 1 to 25 that are not in any of the three sets set1, set2, or set3.'''

	tempSet = set()
	for i in range(1,26):
		tempSet.add(i)

	setE = tempSet - setOne - setTwo - setThree
	
	return setE

def letterF(setOne: set, setTwo: set, setThree: set)->set:
	'''Create a new set of integer elements in the range 1 to 25 that are not in all three sets set1, set2, and set3.'''

	tempSet = set()
	for i in range(1,26):
		tempSet.add(i)

	setF = tempSet | setOne | setTwo | setThree

	return setF

def displaySets(setA: set, setB: set, setC: set, setD: set, setE: set, setF: set)->None:
	'''Displays sets a-f'''
	print("a.", setA)
	print("b.", setB)
	print("c.", setC)
	print("d.", setD)
	print("e.", setE)
	print("f.", setF)

# Main Function -- Call other functions
def main():
	setOne = {1,2,3,4,5}
	setTwo = {2,4,6,8}
	setThree = {1,5,9,13,17}

	setA = letterA(setOne, setTwo)
	setB = letterB(setOne, setTwo, setThree)
	setC = letterC(setOne, setTwo, setThree)
	setD = letterD(setOne)
	setE = letterE(setOne, setTwo, setThree)
	setF = letterF(setOne, setTwo, setThree)

	displaySets(setA, setB, setC, setD, setE, setF)
	

#Input data by user
	# Within function readValues()
#Processing / Calculations
	# Within Functions
#User Output
	# Above within function


if __name__ == "__main__":
	main()

## Test Run 1 for Q5
# a. {1, 3, 5, 6, 8}
# b. {17, 3, 6, 8, 9, 13}
# c. {1, 2, 4, 5}
# d. {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
# e. {7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25}
# f. {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
