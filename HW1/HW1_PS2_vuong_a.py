#Alan Vuong
#Student ID: 1166772
#Homework 1 Program Set 2
#This program simulates a stock transaction program that allows users to input
#information about the stock and displays the stock information post-purchase.

#data/input
stockName = input("Enter Stock name: ")
numShares = float(input("Enter number of shares : "))
purchasePrice = float(input("Enter Purchase price : "))
sellingPrice = float(input("Enter selling price : "))
commission = float(input("Enter commission : "))

# setting all calculation storing variables to float
stockBuyingTotal = float
commissionPaidPurchase = float
stockSellingTotal = float
commissionPaidSale = float
amountProfitLoss = float

#Processing/Calculations
#1) Amount paid for stock: (number of shares bought * purchase price)
stockBuyingTotal = numShares * purchasePrice		# The total amount paid when buying stocks

#2) Commission paid on the purchase: (total amount paid for stocks * commission in percent)
commissionPaidPurchase = stockBuyingTotal * commission

#3) Amount the stock sold for: (number of shares * selling price) --> Total amount of money spent on buying stock
stockSellingTotal = numShares * sellingPrice		# The total amount received when selling stocks

#4) Commission paid on the sale: (total amount shares sold for * commission in percent)
commissionPaidSale = stockSellingTotal * commission

#5) Profit (or loss if negative): Profit/loss = (amount for sold stocks - commission) - (amount paid to buy stocks + commission)
amountProfitLoss = (stockSellingTotal - commissionPaidSale) - (stockBuyingTotal + commissionPaidPurchase)

#User Output
print("\n\nAmount paid for the stock:" + '{:>11}'.format("$") + '{:>13,.2f}'.format(stockBuyingTotal))
print("Commission paid on the purchase:" + '    $' + '{:>13,.2f}'.format(commissionPaidPurchase))
print("Amount the stock sold for:" + '          $' + '{:>13,.2f}'.format(stockSellingTotal))
print("Commission paid on the sale:" + '        $' + '{:>13,.2f}'.format(commissionPaidSale))
print("Profit (or loss if negative:" + '        $' + '{:13,.2f}'.format(amountProfitLoss))

#ask user to stop program
input('\nPress enter key to quit')

## Test Outputs (5 Test Runs)
## Test Run 1
## Enter Stock name: Kaplack, Inc.
## Enter number of shares : 10000
## Enter Purchase price : 33.92
## Enter selling price : 35.92
## Enter commission : 0.04
## 
## 
## Amount paid for the stock:          $   339,200.00
## Commission paid on the purchase:    $    13,568.00
## Amount the stock sold for:          $   359,200.00
## Commission paid on the sale:        $    14,368.00
## Profit (or loss if negative:        $    -7,936.00
## 
## Press enter key to quit

## Test Run 2
## Enter Stock name: IBM
## Enter number of shares : 15000
## Enter Purchase price : 50.25
## Enter selling price : 100.20
## Enter commission : 0.02
## 
## 
## Amount paid for the stock:          $   753,750.00
## Commission paid on the purchase:    $    15,075.00
## Amount the stock sold for:          $ 1,503,000.00
## Commission paid on the sale:        $    30,060.00
## Profit (or loss if negative:        $   704,115.00
## 
## Press enter key to quit

## Test Run 3
## Enter Stock name: Twitter    
## Enter number of shares : 1000 
## Enter Purchase price : 64.66
## Enter selling price : 72.34
## Enter commission : 0.05
## 
## 
## Amount paid for the stock:          $    64,660.00
## Commission paid on the purchase:    $     3,233.00
## Amount the stock sold for:          $    72,340.00
## Commission paid on the sale:        $     3,617.00
## Profit (or loss if negative:        $       830.00
## 
## Press enter key to quit

## Test Run 4
## Enter Stock name: Facebook, Inc. Common Stock 
## Enter number of shares : 452
## Enter Purchase price : 376.26
## Enter selling price : 402.32
## Enter commission : 0.03
## 
## 
## Amount paid for the stock:          $   170,069.52
## Commission paid on the purchase:    $     5,102.09
## Amount the stock sold for:          $   181,848.64
## Commission paid on the sale:        $     5,455.46
## Profit (or loss if negative:        $     1,221.58
## 
## Press enter key to quit

## Test Run 5
## Enter Stock name: Tesla Inc 
## Enter number of shares : 752
## Enter Purchase price : 733.57
## Enter selling price : 655.32
## Enter commission : 0.02      
## 
## 
## Amount paid for the stock:          $   551,644.64
## Commission paid on the purchase:    $    11,032.89
## Amount the stock sold for:          $   492,800.64
## Commission paid on the sale:        $     9,856.01
## Profit (or loss if negative:        $   -79,732.91
## 
## Press enter key to quit