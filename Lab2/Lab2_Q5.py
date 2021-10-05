#Lab2 Question 5
#Alan Vuong
#Description of Program: This program prints an x number of horizontal asterisks depending on the user input. This input will always be an int.  

#Input data by user
num_asterisks = int(input("How many stars you want? "))

# Processing
i = 0
while i < num_asterisks :
    print('*', end='')
    i = i + 1

## Test Run 1 for Q5
## How many stars you want? 20
## ********************
## 
## Test Run 2 for Q5
## How many stars you want? 10
## **********
## 
## Test Run 3 for Q5
## How many stars you want? 2
## **