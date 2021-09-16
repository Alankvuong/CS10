#Lab1 Question 4
#Alan Vuong
#Description of Program: This program calculates the area and volume of a cylinder from user inputted values

#Input data by user
radius = float(input("Enter the radius of a cylinder: "))
length = float(input("Enter the length of a cylinder: "))

#Constants
PI = 3.141

#Calculation of area and volume 
area = radius * radius * PI
volume = area * length

#User Output 
print("The area is", area)
print("The volume is", volume)

#ask user to quit program
input('\n\nPress the enter key to quit\n\n')

##Test run 1
##Enter the radius of a cylinder: 5.5
##Enter the length of a cylinder: 12
##The area is 95.01525
##The volume is 1140.183
##
##
##Press the enter key to quit
##
##
#Test run 2 for Q1
##Enter the radius of a cylinder: 4.2
##Enter the length of a cylinder: 15 
##The area is 55.40724
##The volume is 831.1086
##
##
##Press the enter key to quit
##
##
#Test run 3 for Q1
##Enter the radius of a cylinder: 6.5
##Enter the length of a cylinder: 18
##The area is 132.70725
##The volume is 2388.7304999999997
##
##
##Press the enter key to quit
##
##

