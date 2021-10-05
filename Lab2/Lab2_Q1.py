#Lab2 Question 1
#Alan Vuong
#Description of Program: This program determines whether a person is eligible to vote or not. If they are not elegible, then display how many years are left until they are elegible.

#Input data by user
user_age = int(input("Enter the age: "))

#Calculations and User Output
if user_age < 18:
    years_remaining = 18 - user_age
    print("You have to wait another " + str(years_remaining) + " years to cast your vote")
elif user_age >= 18:
    print("You are eligible to cast your vote")

# User Output -- Above ^

## Test Run 1 for Q1
## Enter the age: 10
## You have to wait another 8 years to cast your vote
## 
## Test Run 2 for Q1
## Enter the age: 25
## You are eligible to cast your vote
## 
## Test Run 3 for Q1
## Enter the age: 16
## You have to wait another 2 years to cast your vote