#Alan Vuong
#Student ID: 1166772
#Homework 3 Program Set 1
#This program simulates a stock transaction program that allows users to input information about the stock and displays the stock information post-purchase using functions.

# User input
def getStockName()->str:
	'''This function gets the name of the stock'''

	stockName = input("\nEnter Stock name: ")

	return stockName


def getNumShares()->int:
	'''This function gets the number of shares the user wants to buy'''

	numShares = int(input("Enter Number of shares : "))

	return numShares


def getStockBuySellPrice()->float:
	'''This function gets the purchase price and selling price of the stock set by the user'''

	purchasePrice = float(input("Enter Purchase price : "))
	sellingPrice = float(input("Enter selling price : "))
	
	return purchasePrice, sellingPrice


def getCommission()->float:
	'''This function gets the commission rate from buying or selling the stock'''

	commission = float(input("Enter Commission : "))

	return commission


# Calculations
def calcStockPurchaseTotal(numShares: int, purchasePrice: float)->float:
	''' This function calculates the total amount paid for the stock'''

	stockBuyingTotal = numShares * purchasePrice		# The total amount paid when buying stocks

	return stockBuyingTotal


def calcCommission(stockBuySellTotal: float, commission: float)->float:
	'''This function calculates the commission from buying or selling the stock
	'''
	# Commission paid on purchase: (total amount paid/sold for stocks * commission in percent)
	transactionCommission = stockBuySellTotal * commission

	return transactionCommission


def calcStockSellingTotal(numShares: int, sellingPrice: float)->float:
	'''This function caclulates the total amount received from selling the stocks'''
	stockSellingTotal = numShares * sellingPrice		# The total amount received when selling stocks

	return stockSellingTotal


def calcProfit(calcStockSellingTotal: float, commissionFromSell: float, stockPurchaseTotal: float, commissionFromPurchase: float)->float:
	'''This function calculates the net profit from buying and selling the stock with commission'''
	netProfit = (calcStockSellingTotal - commissionFromSell) - (stockPurchaseTotal + commissionFromPurchase)

	return netProfit


# User Output
def displayStockInfo(stockName: str, stockPurchaseTotal: float, commissionFromPurchase: float, stockSellTotal: float, commissionFromSell: float, netProfit: float)->None:
	'''This function displays all the necessary info to the user'''
	
	print("\n\nStock name : " + stockName)
	print("Amount paid for the stock:" + '{:>11}'.format("$") + '{:>13,.2f}'.format(stockPurchaseTotal))
	print("Commission paid on the purchase:" + '    $' + '{:>13,.2f}'.format(commissionFromPurchase))
	print("Amount the stock sold for:" + '          $' + '{:>13,.2f}'.format(stockSellTotal))
	print("Commission paid on the sale:" + '        $' + '{:>13,.2f}'.format(commissionFromSell))
	print("Profit (or loss if negative):" + '        $' + '{:13,.2f}'.format(netProfit))


def main():
	userInitPurchase = input("Enter your stock information? Type 'y' for yes, or 'n' for no: ")

	while(userInitPurchase == 'y' or userInitPurchase == 'Y'):
		stockName = getStockName()
		numShares = getNumShares()
		purchasePrice, sellingPrice = getStockBuySellPrice()
		commission = getCommission()

		stockPurchaseTotal = calcStockPurchaseTotal(numShares, purchasePrice)
		# print(stockPurchaseTotal)
		commissionFromPurchase = calcCommission(stockPurchaseTotal, commission)
		# print(commissionFromPurchase)

		stockSellTotal = calcStockSellingTotal(numShares, sellingPrice)
		# print(stockSellTotal)

		commissionFromSell = calcCommission(stockSellTotal, commission)
		netProfit = calcProfit(stockSellTotal, commissionFromSell, stockPurchaseTotal, commissionFromPurchase)

		displayStockInfo(stockName, stockPurchaseTotal, commissionFromPurchase, stockSellTotal, commissionFromSell, netProfit)

		userInitPurchase = input("\n\nEnter your stock information? Type 'y' for yes, or 'n' for no: ")


if __name__ == "__main__":
	main()

## Test Outputs (5 Test Runs)
## Test Run 1
## Enter your stock information? Type 'y' for yes, or 'n' for no: y

## Enter Stock name: Kaplack, Inc.
## Enter number of shares : 10000
## Enter Purchase price : 33.92
## Enter selling price : 35.92
## Enter commission : 0.04


## Stock name : Kaplack, Inc.
## Amount paid for the stock:          $   339,200.00
## Commission paid on the purchase:    $    13,568.00
## Amount the stock sold for:          $   359,200.00
## Commission paid on the sale:        $    14,368.00
## Profit (or loss if negative:        $    -7,936.00


## Enter your stock information? Type 'y' for yes, or 'n' for no: y

## Enter Stock name: IBM
## Enter number of shares : 15000
## Enter Purchase price : 50.25
## Enter selling price : 100.20
## Enter commission : 0.02


## Stock name : IBM
## Amount paid for the stock:          $   753,750.00
## Commission paid on the purchase:    $    15,075.00
## Amount the stock sold for:          $ 1,503,000.00
## Commission paid on the sale:        $    30,060.00
## Profit (or loss if negative:        $   704,115.00 


## Enter your stock information? Type 'y' for yes, or 'n' for no: n

## Test Run 2
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
 
## Enter Stock name: Twitter
## Enter Number of shares : 1000
## Enter Purchase price : 64.66
## Enter selling price : 72.34
## Enter Commission : 0.05##
 
 
## Stock name : Twitter
## Amount paid for the stock:          $    64,660.00
## Commission paid on the purchase:    $     3,233.00
## Amount the stock sold for:          $    72,340.00
## Commission paid on the sale:        $     3,617.00
## Profit (or loss if negative):       $       830.00


##Enter your stock information? Type 'y' for yes, or 'n' for no: n

## Test Run 3
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
## 
## Enter Stock name: Facebook, Inc. Common Stock
## Enter Number of shares : 452
## Enter Purchase price : 376.26
## Enter selling price : 402.32
## Enter Commission : 0.03
## 
## 
## Stock name : Facebook, Inc. Common Stock
## Amount paid for the stock:          $   170,069.52
## Commission paid on the purchase:    $     5,102.09
## Amount the stock sold for:          $   181,848.64
## Commission paid on the sale:        $     5,455.46
## Profit (or loss if negative):       $     1,221.58
## 
## 
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
## 
## Enter Stock name: Tesla Inc
## Enter Number of shares : 752
## Enter Purchase price : 733.57
## Enter selling price : 655.32
## Enter Commission : 0.02
## 
## 
## Stock name : Tesla Inc
## Amount paid for the stock:          $   551,644.64
## Commission paid on the purchase:    $    11,032.89
## Amount the stock sold for:          $   492,800.64
## Commission paid on the sale:        $     9,856.01
## Profit (or loss if negative):       $   -79,732.91
## 
## 
## Enter your stock information? Type 'y' for yes, or 'n' for no: n

## Test Run 4
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
## 
## Enter Stock name: Amazon.com, Inc.
## Enter Number of shares : 18
## Enter Purchase price : 3335.55
## Enter selling price : 3210.26
## Enter Commission : 0.06
## 
## 
## Stock name : Amazon.com, Inc.
## Amount paid for the stock:          $    60,039.90
## Commission paid on the purchase:    $     3,602.39
## Amount the stock sold for:          $    57,784.68
## Commission paid on the sale:        $     3,467.08
## Profit (or loss if negative):       $    -9,324.69
## 
## 
## Enter your stock information? Type 'y' for yes, or 'n' for no: n

## Test Run 5
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
## 
## Enter Stock name: Alphabet Inc Class A
## Enter Number of shares : 6
## Enter Purchase price : 2751.33
## Enter selling price : 2981.44
## Enter Commission : 0.03
## 
## 
## Stock name : Alphabet Inc Class A
## Amount paid for the stock:          $    16,507.98
## Commission paid on the purchase:    $       495.24
## Amount the stock sold for:          $    17,888.64
## Commission paid on the sale:        $       536.66
## Profit (or loss if negative):       $       348.76
## 
## 
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
## 
## Enter Stock name: Snap Inc
## Enter Number of shares : 24 
## Enter Purchase price : 55.14
## Enter selling price : 49.21
## Enter Commission : 0.08
## 
## 
## Stock name : Snap Inc
## Amount paid for the stock:          $     1,323.36
## Commission paid on the purchase:    $       105.87
## Amount the stock sold for:          $     1,181.04
## Commission paid on the sale:        $        94.48
## Profit (or loss if negative):       $      -342.67
## 
## 
## Enter your stock information? Type 'y' for yes, or 'n' for no: n