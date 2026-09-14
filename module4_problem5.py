#Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
#Enter "help" below or click "Help" above for more information.






###Problem 5 in Module 3/4 Assignment
#Input the purchase price per share, the current stock price and quantity of stock,
#compute the increase (or decrease) of the value of the stock entered. (Value is
#computed as (current price – price per share) * quantity. If the amount is negative
#that means you are losing money).

##variables purchase price per share, current stock price, quantity of stock

share_purchase_price = float(input("Share price at time of purchase: "))
current_stock_price = float(input("Current stock price: "))
stock_quantity = float(input("Quantity of stock purchased: "))

amount_difference = current_stock_price - (stock_quantity * share_purchase_price)


if amount_difference >= 0:
    print(f"${amount_difference:.2f} increase")
else:
    print(f"$ {abs(amount_difference):.2f} decrease")


