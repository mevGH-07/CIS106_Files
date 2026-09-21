##Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
##Enter "help" below or click "Help" above for more information.





##Problem 2
##The input to the problem is quantity of widgets. Your program should
###determine the price to charge based on the schedule below. Calculate the
##extended price (quantity x price). Calculate tax at 7%. Display the
##extended price, tax amount and total.
##Quantity Price
##>10000 $10
##5000 to 10000 $20
##Below 5000 $30


widget_qty = float(input("Quantity of Widgets: "))
widget_price = float(10 if widget_qty > 10000 else 30 if widget_qty < 5000 else 20)
widget_extprice = widget_qty * widget_price
widget_tax = widget_extprice * float(.07)
widget_total = widget_extprice + widget_tax


print(f"Quantity: {widget_qty:.0f} units")
print(f"Unit Price: ${widget_price:.2f}")
print(f"Extended Price: ${widget_extprice:.2f}")
print(f"Tax: ${widget_tax:.2f}")
print(f"Total: ${widget_total:.2f}")


