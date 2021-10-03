#Lab2 Question 5
#Alan Vuong
#Description of Program: This program prints an x number of horizontal asterisks depending on the user input. This input will always be an int.  

#Input data by user
num_asterisks = int(input("How many stars you want? "))

#Calculations
i = 0

while i < num_asterisks :
    print('*', sep=' ', end='', flush=True)
    i = i + 1

##Test Run 1 for Q5
