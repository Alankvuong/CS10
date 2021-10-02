#Alan Vuong
#Student ID: 1166772
#Homework 2 Program Set 2
#This program will allow users to compare the taxes they have to pay in 2018 compared to 2017. They will first input their income,
#and we will calculate the taxes for the two years as well as the percent difference and output it to the user. The 
#user will continue to be prompted until a negative income is entered, signaling the end of the program.

#input
userIncome = int(input("Enter income as an integer with no commas: "))

#Calculations
taxed_userIncome = None
difference = None
percent_difference = None
taxSum_2018 = 0
taxSum_2017 = 0

while userIncome >= 0:
	#For 2017
	if userIncome <= 9325:
		firstBracket_userIncome = userIncome						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
	elif userIncome >= 9326 and userIncome <= 37950:
		newUserIncome = userIncome								# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9325						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = userIncome - 9325			# Calculates the range for the second tax bracket
		taxed_userIncome = secondBracket_userIncome * 0.15		# Multiplies the income by the tax percentage of the bracket
		taxSum_2017 += taxed_userIncome							# Adds taxed amount to a variable
		newUserIncome -= secondBracket_userIncome				# Subtracts the original income from the range of bracket
	elif userIncome >= 37951 and userIncome <= 91900:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9325						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 37950 - 9325
		taxed_userIncome = secondBracket_userIncome * 0.15
		taxSum_2017 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = userIncome - 37950
		taxed_userIncome = thirdBracket_userIncome * 0.25
		taxSum_2017 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome
	elif userIncome >= 91901 and userIncome <= 191650:	
		#1) Find the range of the corrresponding income bracket
		#2) Multiply the range by the percentage that it is taxed
		#3) Add the found value (the taxed amount) to a variable
		#4) Subtract the range from the original income amount

		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9325						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 37950 - 9325
		taxed_userIncome = secondBracket_userIncome * 0.15
		taxSum_2017 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 91900 - 37950
		taxed_userIncome = thirdBracket_userIncome * 0.25
		taxSum_2017 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = userIncome - 91900
		taxed_userIncome = fourthBracket_userIncome * 0.28
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome
	elif userIncome >= 191651 and userIncome <= 416700	:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9325						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 37950 - 9325
		taxed_userIncome = secondBracket_userIncome * 0.15
		taxSum_2017 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 91900 - 37950
		taxed_userIncome = thirdBracket_userIncome * 0.25
		taxSum_2017 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = 191650 - 91900
		taxed_userIncome = fourthBracket_userIncome * 0.28
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fifthBracket_userIncome = userIncome - 191650
		taxed_userIncome = fifthBracket_userIncome * 0.33
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fifthBracket_userIncome
	elif userIncome >= 416701 and userIncome <= 418400	:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9325						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 37950 - 9325
		taxed_userIncome = secondBracket_userIncome * 0.15
		taxSum_2017 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 91900 - 37950
		taxed_userIncome = thirdBracket_userIncome * 0.25
		taxSum_2017 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = 191650 - 91900
		taxed_userIncome = fourthBracket_userIncome * 0.28
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fifthBracket_userIncome = 416700 - 191650
		taxed_userIncome = fifthBracket_userIncome * 0.33
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fifthBracket_userIncome

		sixthBracket_userIncome = userIncome - 416700
		taxed_userIncome = sixthBracket_userIncome * 0.35
		taxSum_2017 += taxed_userIncome
		newUserIncome -= sixthBracket_userIncome
	elif userIncome > 418400:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9325						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2017 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 37950 - 9325
		taxed_userIncome = secondBracket_userIncome * 0.15
		taxSum_2017 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 91900 - 37950
		taxed_userIncome = thirdBracket_userIncome * 0.25
		taxSum_2017 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = 191650 - 91900
		taxed_userIncome = fourthBracket_userIncome * 0.28
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fifthBracket_userIncome = 416700 - 191650
		taxed_userIncome = fifthBracket_userIncome * 0.33
		taxSum_2017 += taxed_userIncome
		newUserIncome -= fifthBracket_userIncome

		sixthBracket_userIncome = 418400 - 416700
		taxed_userIncome = sixthBracket_userIncome * 0.35
		taxSum_2017 += taxed_userIncome
		newUserIncome -= sixthBracket_userIncome

		seventhBracket_userIncome = userIncome - 418400
		taxed_userIncome = seventhBracket_userIncome * 0.396
		taxSum_2017 += taxed_userIncome
		newUserIncome -= seventhBracket_userIncome

	# For 2018
	if userIncome <= 9525:
		firstBracket_userIncome = userIncome						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
	elif userIncome >= 9526 and userIncome <= 38700:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9525						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = userIncome - 9525
		taxed_userIncome = secondBracket_userIncome * 0.12
		taxSum_2018 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome
	elif userIncome >= 38701 and userIncome <= 82500:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9525						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 38700 - 9525
		taxed_userIncome = secondBracket_userIncome * 0.12
		taxSum_2018 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = userIncome - 38700
		taxed_userIncome = thirdBracket_userIncome * 0.22
		taxSum_2018 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome
	elif userIncome >= 82501 and userIncome <= 157500:	
		#1) Find the range of the corrresponding income bracket
		#2) Multiply the range by the percentage that it is taxed
		#3) Add the found value (the taxed amount) to a variable
		#4) Subtract the range from the original income amount

		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9525						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 38700 - 9525
		taxed_userIncome = secondBracket_userIncome * 0.12
		taxSum_2018 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 82500 - 38700
		taxed_userIncome = thirdBracket_userIncome * 0.22
		taxSum_2018 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = userIncome - 82500
		taxed_userIncome = fourthBracket_userIncome * 0.24
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome
	elif userIncome >= 157501 and userIncome <= 200000:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9525						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 38700 - 9525
		taxed_userIncome = secondBracket_userIncome * 0.12
		taxSum_2018 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 82500 - 38700
		taxed_userIncome = thirdBracket_userIncome * 0.22
		taxSum_2018 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = 157500 - 82500
		taxed_userIncome = fourthBracket_userIncome * 0.24
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fourthBracket_userIncome = userIncome - 157500
		taxed_userIncome = fourthBracket_userIncome * 0.32
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome
	elif userIncome >= 200001 and userIncome <= 500000:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9525						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 38700 - 9525
		taxed_userIncome = secondBracket_userIncome * 0.12
		taxSum_2018 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 82500 - 38700
		taxed_userIncome = thirdBracket_userIncome * 0.22
		taxSum_2018 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = 157500 - 82500
		taxed_userIncome = fourthBracket_userIncome * 0.24
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fourthBracket_userIncome = 200000 - 157500
		taxed_userIncome = fourthBracket_userIncome * 0.32
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fifthBracket_userIncome = userIncome - 200000
		taxed_userIncome = fifthBracket_userIncome * 0.35
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fifthBracket_userIncome
	elif userIncome > 500000:
		newUserIncome = userIncome				# Sets newUserIncome as a placeholder for original userIncome
		firstBracket_userIncome = 9525						
		taxed_userIncome = firstBracket_userIncome * 0.10		# Find the amount taxed based on range of bracket
		taxSum_2018 += taxed_userIncome							# Add taxed amount to a storage variable
		newUserIncome -= firstBracket_userIncome				# Subtract the original amount by the range of the bracket

		secondBracket_userIncome = 38700 - 9525
		taxed_userIncome = secondBracket_userIncome * 0.12
		taxSum_2018 += taxed_userIncome
		newUserIncome -= secondBracket_userIncome

		thirdBracket_userIncome = 82500 - 38700
		taxed_userIncome = thirdBracket_userIncome * 0.22
		taxSum_2018 += taxed_userIncome
		newUserIncome -= thirdBracket_userIncome

		fourthBracket_userIncome = 157500 - 82500
		taxed_userIncome = fourthBracket_userIncome * 0.24
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fourthBracket_userIncome = 200000 - 157500
		taxed_userIncome = fourthBracket_userIncome * 0.32
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fourthBracket_userIncome

		fifthBracket_userIncome = 500000 - 200000
		taxed_userIncome = fifthBracket_userIncome * 0.35
		taxSum_2018 += taxed_userIncome
		newUserIncome -= fifthBracket_userIncome

		sixthBracket_userIncome = userIncome - 500000
		taxed_userIncome = sixthBracket_userIncome * 0.37
		taxSum_2018 += taxed_userIncome
		newUserIncome -= sixthBracket_userIncome

	difference = taxSum_2018 - taxSum_2017										# Finds the difference between the two years
	percent_difference = ((taxSum_2018 - taxSum_2017) / taxSum_2017) * -100		# Finds the percent difference, multiply by negative 

	if(percent_difference == 0):						# 0 cannot be a negative number
		percent_difference = 0

	#User Output
	print("Income: " + str(userIncome))
	print("2017 tax: " + '{:.2f}'.format(taxSum_2017))
	print("2018 tax: " + '{:.2f}'.format(taxSum_2018))
	print("Difference: " + '{:.2f}'.format(difference))
	print("Difference (percent): " + '{:.2f}'.format(percent_difference))

	userIncome = int(input("\nEnter income as an integer with no commas: "))

	# reinitialzing used variables to empty variable
	taxed_userIncome = None
	difference = None
	percent_difference = None
	taxSum_2018 = 0
	taxSum_2017 = 0

## Output
## Test Run 1
## Enter income as an integer with no commas: 8000
## Income: 8000
## 2017 tax: 800.00
## 2018 tax: 800.00
## Difference: 0.00
## Difference (percent): 0.00

## Enter income as an integer with no commas: 15000
## Income: 15000
## 2017 tax: 1783.75
## 2018 tax: 1609.50
## Difference: -174.25
## Difference (percent): 9.77

## Enter income as an integer with no commas: 40000
## Income: 40000
## 2017 tax: 5738.75
## 2018 tax: 4739.50
## Difference: -999.25
## Difference (percent): 17.41

## Enter income as an integer with no commas: 100000
## Income: 100000    
## 2017 tax: 20981.75
## 2018 tax: 18289.50
## Difference: -2692.25
## Difference (percent): 12.83

## Enter income as an integer with no commas: 200000
## Income: 200000
## 2017 tax: 49399.25
## 2018 tax: 45689.50
## Difference: -3709.75
## Difference (percent): 7.51

## Enter income as an integer with no commas: 500000
## Income: 500000
## 2017 tax: 153818.85
## 2018 tax: 150689.50
## Difference: -3129.35
## Difference (percent): 2.03

## Enter income as an integer with no commas: 1000000
## Income: 1000000
## 2017 tax: 351818.85
## 2018 tax: 335689.50
## Difference: -16129.35
## Difference (percent): 4.58

## Enter income as an integer with no commas: 10000000
## Income: 10000000
## 2017 tax: 3915818.85
## 2018 tax: 3665689.50
## Difference: -250129.35
## Difference (percent): 6.39

## Enter income as an integer with no commas: -1

## Test Run 2
## Enter income as an integer with no commas: -1

## Test Run 3
## Enter income as an integer with no commas: 45000
## Income: 45000
## 2017 tax: 6988.75
## 2018 tax: 5839.50
## Difference: -1149.25
## Difference (percent): 16.44

## Enter income as an integer with no commas: 122000
## Income: 122000
## 2017 tax: 27141.75
## 2018 tax: 23569.50
## Difference: -3572.25
## Difference (percent): 13.16

## Enter income as an integer with no commas: 842000
## Income: 842000
## 2017 tax: 289250.85
## 2018 tax: 277229.50
## Difference: -12021.35
## Difference (percent): 4.16

## Enter income as an integer with no commas: 10000
## Income: 10000
## 2017 tax: 1033.75
## 2018 tax: 1009.50
## Difference: -24.25
## Difference (percent): 2.35

## Enter income as an integer with no commas: -1

## Test Run 4
## Enter income as an integer with no commas: 23220
## Income: 23220
## 2017 tax: 3016.75
## 2018 tax: 2595.90
## Difference: -420.85
## Difference (percent): 13.95

## Enter income as an integer with no commas: 58000
## Income: 58000
## 2017 tax: 10238.75
## 2018 tax: 8699.50
## Difference: -1539.25
## Difference (percent): 15.03

## Enter income as an integer with no commas: 9102
## Income: 9102
## 2017 tax: 910.20
## 2018 tax: 910.20
## Difference: 0.00
## Difference (percent): 0.00

## Enter income as an integer with no commas: 191651
## Income: 191651
## 2017 tax: 46644.08
## 2018 tax: 43017.82
## Difference: -3626.26
## Difference (percent): 7.77

## Enter income as an integer with no commas: 416824
## Income: 416824
## 2017 tax: 120953.65
## 2018 tax: 121577.90
## Difference: 624.25
## Difference (percent): -0.52

## Enter income as an integer with no commas: -1

## Test Run 5
## Enter income as an integer with no commas: 82501
## Income: 82501
## 2017 tax: 16364.00
## 2018 tax: 14089.74
## Difference: -2274.26
## Difference (percent): 13.90
 
## Enter income as an integer with no commas: 168240
## Income: 168240
## 2017 tax: 40088.95
## 2018 tax: 35526.30
## Difference: -4562.65
## Difference (percent): 11.38
 
## Enter income as an integer with no commas: 26450 
## Income: 26450
## 2017 tax: 3501.25
## 2018 tax: 2983.50
## Difference: -517.75
## Difference (percent): 14.79
 
## Enter income as an integer with no commas: 8900
## Income: 8900
## 2017 tax: 890.00
## 2018 tax: 890.00
## Difference: 0.00
## Difference (percent): 0.00
 
## Enter income as an integer with no commas: -1