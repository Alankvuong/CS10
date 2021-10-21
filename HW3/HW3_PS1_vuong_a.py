#Alan Vuong
#Student ID: 1166772
#Homework 2 Program Set 1
# This program 

def getStockName()->str:
	'''This function gets the name of the stock'''

	stockName = input("\nEnter Stock name: ")

	return stockName

def getNumShares()->int:
	'''This function gets the number of shares the user wants to buy'''

	numShares = int(input("Enter number of shares : "))

	return numShares

def getStockBuySellPrice()->float:
	'''This function gets the purchase price and selling price of the stock set by the user'''

	purchasePrice = float(input("Enter Purchase price : "))
	sellingPrice = float(input("Enter selling price : "))
	
	return purchasePrice, sellingPrice

def getCommission()->float:
	'''This function gets the commission rate from buying or selling the stock'''

	commission = float(input("Enter commission : "))

	return commission

def calcStockPurchaseTotal(numShares: int, purchasePrice: float)-> float:
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

def displayStockInfo(stockName: str, stockPurchaseTotal: float, commissionFromPurchase: float, stockSellTotal: float, commissionFromSell: float, netProfit: float)->None:
	'''This function displays all the necessary info to the user'''
	
	print("\n\nStock name : " + stockName)
	print("Amount paid for the stock:" + '{:>11}'.format("$") + '{:>13,.2f}'.format(stockPurchaseTotal))
	print("Commission paid on the purchase:" + '    $' + '{:>13,.2f}'.format(commissionFromPurchase))
	print("Amount the stock sold for:" + '          $' + '{:>13,.2f}'.format(stockSellTotal))
	print("Commission paid on the sale:" + '        $' + '{:>13,.2f}'.format(commissionFromSell))
	print("Profit (or loss if negative:" + '        $' + '{:13,.2f}'.format(netProfit))

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
