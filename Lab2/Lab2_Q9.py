#Lab2 Question 9
#Alan Vuong
#Description of Program: This program uses a for loop to calculate the sum of numbers. The user will specify how many numbers to sum.

#Input data by user
num_numbers = int(input("How many numbers do you want to add? "))

#Initializing variable
sum_numbers = 0

#Processing
for i in range(0, num_numbers):
    add_num = int(input("Enter number " + str(i+1) + " : "))
    sum_numbers = sum_numbers + add_num

#User output
print("The total is " + '{:.1f}'.format(sum_numbers))

## Test Run 1 for Q9
## How many numbers do you want to add? 3
## Enter number 1 : 25
## Enter number 2 : 34
## Enter number 3 : 33
## The total is 92.0

## Test Run 2 for Q9
## How many numbers do you want to add? 4
## Enter number 1 : 10
## Enter number 2 : 20
## Enter number 3 : 30
## Enter number 4 : 40
## The total is 100.0

## Test Run 3 for Q9
## How many numbers do you want to add? 5
## Enter number 1 : 18
## Enter number 2 : 42
## Enter number 3 : 32
## Enter number 4 : 2
## Enter number 5 : 4
## The total is 98.0