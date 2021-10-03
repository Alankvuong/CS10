#Lab2 Question 3
#Alan Vuong
#Description of Program: This program deteremines whether a character entered is a vowel or not.

#Input data by user
char_input = input("Enter any character: ")
isVowel = bool

#Constants
lower_a = 'a'
lower_e = 'e'
lower_i = 'i'
lower_o = 'o'
lower_u = 'u'
upper_a = 'A'
upper_e = 'E'
upper_i = 'I'
upper_o = 'O'
upper_u = 'U'

#Calculation
if (char_input == lower_a or char_input == lower_e or char_input == lower_i or char_input == lower_o or char_input == lower_u):
    isVowel = True
elif(char_input == upper_a or char_input == upper_e or char_input == upper_i or char_input == upper_o or char_input == upper_u):
    isVowel = True
else:
    isVowel = False

#User output
if(isVowel == True):
    print(char_input + " is a vowel")
else:
    print(char_input + " is not a vowel")

##Test Run 1 for Q3
