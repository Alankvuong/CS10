#Lab1 Question 6
#Alan Vuong
#Description of Program: This program asks the user how many cookies they want to make, and then displays the 
# number of cups needed for each ingredient.

#Input data by user
numCookies = int(input("Enter the number of cookies: "))

#Constants (Produces 48 cookies)
SUGAR_REQUIRED = 1.5
BUTTER_REQUIRED = 1.0
FLOUR_REQUIRED = 2.75

#Calculations of sugar, butter, and flour needed
sugarNeeded = (numCookies / 48) * SUGAR_REQUIRED 
butterNeeded = float((numCookies / 48) * BUTTER_REQUIRED)
flourNeeded = (numCookies / 48) * FLOUR_REQUIRED

#User output
print("\nTo make " + format(numCookies, '.1f') + " cookies, you will need:")
print(format(sugarNeeded, '.2f') + " cups of sugar")
print(format(butterNeeded, '.2f') + " cups of butter")
print(format(flourNeeded, '.2f') + " cups of flour")

#ask user to quit program
input('\n\nPress the enter key to quit\n\n')

##Test run 1 for Q2
##Enter the number of cookies: 56
##
##To make 56.0 cookies, you will need:
##1.75 cups of sugar
##1.17 cups of butter
##3.21 cups of flour
##
##
##Press the enter key to quit
##
##
#Test run 2 for Q2
##Enter the number of cookies: 48
##
##To make 48.0 cookies, you will need:
##1.50 cups of sugar
##1.00 cups of butter
##2.75 cups of flour
##
##
##Press the enter key to quit
##
##
#Test run 3 for Q2
##Enter the number of cookies: 128
##
##To make 128.0 cookies, you will need:
##4.00 cups of sugar
##2.67 cups of butter
##7.33 cups of flour
##
##
##Press the enter key to quit
##
##