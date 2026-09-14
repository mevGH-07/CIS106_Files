#Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
#Enter "help" below or click "Help" above for more information.


###Problem 2 in Module 3/4 Assignment
#Allow the user to enter the stock ticker symbol (ie MSFT for Microsoft), number of
#shares and cost per share. Compute and display amount invested to be number
#of shares times cost per share.

#input stock ticker symbol
stock_symbol = input("Please enter in Stock Symbol: ")

#input number of share

share_number = float(input ("Enter in number of shares: "))

#input cost per share

share_cost = float(input("Enter in the cost per share: "))

#total amount invested is number of share * cost per share
amount_invested = share_cost * share_number

print(f"Total amount invested in {stock_symbol}: ${amount_invested:.2f}")




