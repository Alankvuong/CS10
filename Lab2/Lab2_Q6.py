#Lab2 Question 6
#Alan Vuong
#Description of Program: This program calculates a property tax. The user will enter a lot number and property value, and the program will calculate the total property tax value. Tax Factor = 0.0065, property tax = property value * tax factor

print("Enter the property lot number or enter -999 to end")

#Input data by user
lot_num = int(input("Enter the lot number: "))

#Processing / Calculations
while lot_num != -999:
    property_value = float(input("Enter property value: "))

    #Constants
    tax_factor = 0.0065

    #Calculations
    property_tax = property_value * tax_factor

    #User output
    print("Property tax: $" + '{:.2f}'.format(property_tax))

    print("\nEnter the property lot number or enter -999 to end")
    lot_num = int(input("Enter the lot number: "))

##Test Run 1 for Q6
## Enter the property lot number or enter -999 to end
## Enter the lot number: 100
## Enter property value: 100000.00
## Property tax: $650.00
## 
## Enter the property lot number or enter -999 to end
## Enter the lot number: 200
## Enter property value: 5000.00
## Property tax: $32.50
## 
## Enter the property lot number or enter -999 to end
## Enter the lot number: -999

## Test Run 2 for Q6
## Enter the property lot number or enter -999 to end
## Enter the lot number: -999

## Test Run 3 for Q6
## Enter the property lot number or enter -999 to end
## Enter the lot number: 400
## Enter property value: 250000.00
## Property tax: $1625.00
## 
## Enter the property lot number or enter -999 to end
## Enter the lot number: 20
## Enter property value: 25000.25
## Property tax: $162.50
## 
## Enter the property lot number or enter -999 to end
## Enter the lot number: -999