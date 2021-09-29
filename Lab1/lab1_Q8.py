#Lab 1 Question 8
#Alan Vuong
#Description: This program calculates the gravitational force and acceleration caused by gravitational force exterted on him by Earth after being provided a mass (m).

#input data by user
mass = float(input("Enter a mass in kg: "))

#Constants
RADIUS = (6378 * 10**3)
MASS_1 = (5.9742 * 10**24)
GRAVITY = (6.67300 * 10**-11)

#Calculations of gravity
# Formula: g = [G(m1)(m)/r^2)]/m
g = (((GRAVITY * (MASS_1) * (mass)) / RADIUS**2) / mass)

#User output
print("The resulting value of g is " + format(g, '.4f') + " which is close to the earth's gravitational force.")

#ask user to quit program
input('\n\nPress the enter key to quit\n\n')

##Test Run 1 for Q8
##Enter a mass in kg: 30
##The resulting value of g is 9.8001 which is close to the earth's gravitational force.
##
##
##Press the enter key to quit
##
##
##Test Run 2 for Q8
##Enter a mass in kg: 80
##The resulting value of g is 9.8001 which is close to the earth's gravitational force.
##
##
##Press the enter key to quit
##
##