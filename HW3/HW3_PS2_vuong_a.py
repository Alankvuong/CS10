#Alan Vuong
#Student ID: 1166772
#Homework 3 Program Set 2
# This program will take in a credit card number and verify whether it is valid or invalid. The verification process is known as Luhn Check, or Mod 10 Check.

def isValid(number: str)->bool:
	'''This function will return true if the card number is valid, and false otherwise'''

	numberLength = len(number)		# Gets length to verify if valid or invalid

	if (number.startswith('4') or number.startswith('5') or number.startswith('37') or number.startswith('6')) and (numberLength >= 13 and numberLength <= 16):
		# Function calls to get sum
		sumDoubleEvens = sumOfDoubleEvenPlace(number)
		sumOdds = sumOfOddPlace(number)

		sumOddsAndEven = sumDoubleEvens + sumOdds

		# Checking if the sum above is divisible by 10 (valid)
		if sumOddsAndEven % 10 == 0:
			return True
		else:
			return False
	else:
		return False

 
def sumOfDoubleEvenPlace(cardNumber: str)->int: 
	'''This function finds the even place digits from the given number, doubles each digit, and finds its sum. Returns the sum of doubled numbers.'''

	evensPlaceString = ''			# New string for even place numbers in CC #

	# Loops through all digits to find evens place
	while int(cardNumber) > 0:
		last_cardNumber = int(cardNumber) / 10		# Gets rid of the last digit in number
		evens_digit = int(last_cardNumber) % 10		# Gets every even digit after getting rid of last number
		cardNumber = int(cardNumber) / 100			# Divide by 100 to skip the odds place
		evensPlaceString += str(evens_digit)		# Adds even digit to empty string above

	integer_evens_string = int(evensPlaceString)	# Converts string to int to be used in loop

	sum_evens = 0									# Stores the sum of all even numbers
	# Loops through evens place integers and sums them
	while integer_evens_string > 0:
		digit = integer_evens_string % 10		
		integer_evens_string //= 10				# divide by integers instead of float
		doubledDigit = digit * 2				# Doubles the digit 
		checkedDigit = getDigit(doubledDigit)	# Checks if doubled digit is single or double digit

		sum_evens += checkedDigit				# Adds the digit to sum variable

	return sum_evens		# Returns to original call

def getDigit(number: str)->int: 
	'''This function returns the passed number if it is a single digit, or returns the sum of double digits'''

	sum = 0
	if number < 10:			# if single digit
		return number
	else:					# if double digit
		while number > 0:		# Loop through number to get the sum
			digit = number % 10
			sum += digit
			number = number // 10
		return sum			# Returns the found sum
		

def sumOfOddPlace(cardNumber: str)->int: 
	'''This function returns the sum of the odd placed digits from the card number'''

	sum_odds = 0
	while int(cardNumber) > 0:
		odds_digit = int(cardNumber) % 10		# Finds the odd placed digit
		cardNumber = int(cardNumber) / 100		# Skips the even place
		sum_odds += odds_digit					# Finds sum of odd placed digits
	
	return sum_odds
 
def main():

	amountToCheck = int(input("How many credit card numbers do you want to check? "))
	if amountToCheck > 0:
		cardNumber = input("Enter a credit card number: ")

		# Loops until user specified number
		for i in range(amountToCheck):
			validityCheck = isValid(cardNumber)		# Function call to check validity of number

			if validityCheck == True:
				print(cardNumber + " is valid")		# If valid
			else:
				print(cardNumber + " is invalid")	# If not valid


			i += 1
			
			# To prevent prompt from appearing at end of program
			if i != amountToCheck:
				cardNumber = input("\nEnter a credit card number: ")


if __name__ == "__main__":
	main()

## Test Outputs (5 Test Runs)
## Test Run 1
## How many credit card numbers do you want to check? 2
## Enter a credit card number: 4388576018402626
## 4388576018402626 is invalid 

## Enter a credit card number: 4388576018410707
## 4388576018410707 is valid

## Test Run 2
## How many credit card numbers do you want to check? 0

## Test Run 3
## How many credit card numbers do you want to check? 3
## Enter a credit card number: 12345678
## 12345678 is invalid
 
## Enter a credit card number: 5169769005222217 
## 5169769005222217 is valid   
 
## Enter a credit card number: 6011655276746808
## 6011655276746808 is invalid

## Test Run 4
## How many credit card numbers do you want to check? 5
## Enter a credit card number: 5589845480227046
## 5589845480227046 is valid
## 
## Enter a credit card number: 6011672317321412
## 6011672317321412 is valid
## 
## Enter a credit card number: 374722279969693
## 374722279969693 is invalid
## 
## Enter a credit card number: 4929661251914643
## 4929661251914643 is valid
## 
## Enter a credit card number: 378221807802955
## 378221807802955 is invalid

## Test Run 5
## How many credit card numbers do you want to check? 4
## Enter a credit card number: 4556478016192492
## 4556478016192492 is valid   
## 
## Enter a credit card number: 5171871132296878
## 5171871132296878 is valid   
## 
## Enter a credit card number: 6011598908732983
## 6011598908732983 is invalid 
## 
## Enter a credit card number: 372962159189191
## 372962159189191 is valid
## 
## Enter a credit card number: 349324123828091
## 349324123828091 is invalid