#Lab1 Question 5
#Alan Vuong
#Description of Program: This program calculates the profit that will be made from a projected amount of total sales

#Input data by user
projectedSales = float(input("Enter the projected total sales: "))

#Calculation of profit projected
profit = projectedSales * .24

#User output
print("The profit made from this amount: " + '{:,.2f}'.format(profit))

#ask user to quit program
input('\n\nPress the enter key to quit\n\n')

##Test run 1 for Q5
##Enter the projected total sales: 1250.00 
##The profit made from this amount: 300.00
##
##
##Press the enter key to quit
##
##
#Test run 2 for Q5
##Enter the projected total sales: 2200.00
##The profit made from this amount: 528.00
##
##
##Press the enter key to quit
##
##
#Test run 3 for Q5
##Enter the projected total sales: 3420.00
##The profit made from this amount: 820.80
##
##
##Press the enter key to quit
##
##