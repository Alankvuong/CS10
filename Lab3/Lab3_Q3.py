#Lab3 Question 3
#Alan Vuong
#Description of Program: This program calculates the area of a right-angled triangle using functions and parameters.

# Functions

#Input data by user
def getData()-> int:
	'''Gets user input for base and height of triangle'''

	base = int(input("Enter the base of your triangle: "))
	height = int(input("Enter the height of your triangle: "))
	
	return base, height

#Processing / Calculations
def trigArea(base: int, height: int)->int: 
	'''Calculates the area of the triangle from the base and height'''

	area = (base * height) / 2
	
	return area

#User Output
def displayData(base: int, height: int, area: int)->None:
	'''Displays the data inputted and the area calculated'''

	print("The base, height, and area are " + '{:.2f}'.format(base) + " , " + '{:.2f}'.format(height) + " , " + '{:.2f}'.format(area))


# Main Function -- Call other functions
def main():
	base, height = getData()
	area = trigArea(base, height)
	displayData(base, height, area)


if __name__ == "__main__":
	main()

## Test Run 1 for Q2
# Enter the base of your triangle: 10
# Enter the height of your triangle: 5
# The base, height, and area are 10.00 , 5.00 , 25.00

## Test Run 2 for Q1
# Enter the base of your triangle: 2
# Enter the height of your triangle: 3
# The base, height, and area are 2.00 , 3.00 , 3.00

## Test Run 3 for Q1
# Enter the base of your triangle: 4
# Enter the height of your triangle: 8
# The base, height, and area are 4.00 , 8.00 , 16.00