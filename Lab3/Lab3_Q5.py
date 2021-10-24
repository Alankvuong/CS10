#Lab 3 Question 5
#Alan Vuong
#Description of Program: This program asks the user to enter a single digit number sequentially without any spaces. The number must be inputted as a string. Then display the sum of the single digit numbers in a single digit string.

# Functions
#Processing / Calculations
def string_total(number_string: str)->str:
    '''This function accepts a number string as a parameter and 
       finds the sum of the digits within the string.'''
    sum_digits = 0

    for digit in number_string:     # Extracts each digit from string
        sum_digits += int(digit)     # Converts digit to int to be added

    sum_digit_string = str(sum_digits) # Converts sum back to string to be displayed

    return sum_digit_string


# Main Function -- Call other functions
def main(): 
    # Get a string of numbers as input from the user. 
    number_string = input('Enter a sequence of digits with nothing separating them: ') 

    # Call string_total function, and store the total. 
    total = string_total(number_string) 

    # Display the total. 
    print('The total of the digits in the string you entered is', total)


if __name__ == "__main__":
	main()

## Test Run 1 for Q5
# Enter a sequence of digits with nothing separating them: 4563
# The total of the digits in the string you entered is 18

## Test Run 2 for Q5
# Enter a sequence of digits with nothing separating them: 653214
# The total of the digits in the string you entered is 21

## Test Run 3 for Q5
# Enter a sequence of digits with nothing separating them: 823412
# The total of the digits in the string you entered is 20