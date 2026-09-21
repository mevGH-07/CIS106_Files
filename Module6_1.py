##Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
##Enter "help" below or click "Help" above for more information.

#Allow a user to enter a quantity of an item. If the quantity is greater than
#or equal to 1000, the unit price should be $3.00. For quantities under 1000
#the unit price is $5.00. Compute extended price to be quantity x unit price.
#Compute tax to be 7% of the extended price. The total is computed as
#extended price plus the tax. Display the quantity, unit price, extended
#price, tax and total.

##Problem 1
qty = float(input("Quantity of item: "))
unit_price = float(3 if qty >=1000 else 5)
ext_price = qty * unit_price
tax = ext_price * float(.07)
price_total = ext_price + tax

print(f"Quantity: {qty:.0f} units")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${ext_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${price_total:.2f}")

