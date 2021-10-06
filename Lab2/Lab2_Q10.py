#Lab2 Question 10
#Alan Vuong
#Description of Program: This program will convert speedds from 60 km/h to 130 km/h (in 10 km/h increments) to mph by using a for loop. The formula is: mph = km/h * conversion factor, where conversion factor is 0.6214.

#Input data by user

#Constants
CONVERSION_FACTOR = 0.6214
#Initializing variable
sum_numbers = 0

#User output
print(format("KPH", '17') + "MPH")
print("------------------------------------")

#Processing
for kph in range(60, 140, 10):
    mph = kph * CONVERSION_FACTOR
    print('{:<17}'.format(kph) + '{:.1f}'.format(mph))      # Print conversion from km/h to mph


## Test Run 1 for Q10
## KPH              MPH
## ------------------------------------
## 60               37.3
## 70               43.5
## 80               49.7
## 90               55.9
## 100              62.1
## 110              68.4
## 120              74.6
## 130              80.8
