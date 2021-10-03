#Lab2 Question 6
#Alan Vuong
#Description of Program: This program calculates a property tax. The user will enter a lot number and property value, and the program will calculate the total property tax value. Tax Factor = 0.0065, property tax = property value * tax factor

print("Enter the property lot number or enter -999 to end")

#Input data by user
lot_num = int(input("Enter the lot number: "))

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
