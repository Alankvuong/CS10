#Alan Vuong
#Student ID: 1166772
#Homework 2 Program Set 1
#This program imitates a lottery and generates a two digit number. It then prompts the user to enter a single two-digit number to determine if the user wins. This program loops until the user chooses to stop playing the lottery.

import random   # imports random number library

#input
userInput = int(input("Enter your lottery pick (2 digits) or -999 to quit: "))

# While loop runs until user enters -999
while(userInput != -999):
    #Generate random two-digit number
    lotteryNum = random.randint(10,99)

#Calculations
    # Splits the lottery number into digits
    lotteryDigit_one = lotteryNum // 10
    lotteryDigit_two = lotteryNum % 10

    #Splits the user guess into digits
    userDigit_one = userInput // 10
    userDigit_two = userInput % 10

#Comparing the lottery number with the user's guess

    # if user guess and lottery number matches
    if(userInput == lotteryNum):
        print("Exact match: You win $10,000!\n")
    elif((lotteryDigit_one == userDigit_two) and (lotteryDigit_two == userDigit_one)):      # if both digits are found but are reversed
        print("Match all digits: You win $3,000\n")
    elif((lotteryDigit_one == userDigit_one) or (lotteryDigit_one == userDigit_two)):       # if one digit matches in the user guess
        print("Match one digit: You win $1,000\n")
    elif((lotteryDigit_two == userDigit_one) or (lotteryDigit_two == userDigit_two)):       # if one digit matches in the user guess
        print("Match one digit: You win $1,000\n")
    else:
        print("Sorry no match\n")

    userInput = int(input("Enter your lottery pick ( 2 digits) or -999 to quit: "))           # asks user to input again


## Test Outputs (5 Test Runs)
## Test Run 1
## Enter your lottery pick (2 digits) or -999 to quit: 44
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 23
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 68
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 12
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 45
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999

## Test Run 2
## Enter your lottery pick ( 2 digits) or -999 to quit: 65
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 80
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 41
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 34
## Exact match: You win $10,000!
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 95
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999

## Test Run 3
## Enter your lottery pick (2 digits) or -999 to quit: 10
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 33
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 46
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 81
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 88
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999

## Test Run 4
## Enter your lottery pick (2 digits) or -999 to quit: 15
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 21
## Match all digits: You win $3,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 48
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 62
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 92
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999

## Test Run 5
## Enter your lottery pick (2 digits) or -999 to quit: 99
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 49
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 42
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 38
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 50
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999