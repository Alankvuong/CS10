#Lab2 Question 3
#Alan Vuong
#Description of Program: This program deteremines whether a character entered is a vowel or not.

#Input data by user
char_input = input("Enter any character: ")
isVowel = bool

#Constants
LOWER_A = 'a'
LOWER_E = 'e'
LOWER_I = 'i'
LOWER_O = 'o'
LOWER_U = 'u'
UPPER_A = 'A'
UPPER_E = 'E'
UPPER_I = 'I'
UPPER_O = 'O'
UPPER_U = 'U'

#Processing, checking to see if uppercase or lowercase vowel
if (char_input == LOWER_A or char_input == LOWER_E or char_input == LOWER_I or char_input == LOWER_O or char_input == LOWER_U):
    isVowel = True
elif(char_input == UPPER_A or char_input == UPPER_E or char_input == UPPER_I or char_input == UPPER_O or char_input == UPPER_U):
    isVowel = True
else:
    isVowel = False

#User output
if(isVowel == True):
    print(char_input + " is a vowel")
else:
    print(char_input + " is not a vowel")


## Test Run 1 for Q3
## Enter any character: h
## h is not a vowel
## 
## Test Run 2 for Q3
## Enter any character: e
## e is a vowel
## 
## Test Run 3 for Q3
## Enter any character: k
## k is not a vowel