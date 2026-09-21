##Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
##Enter "help" below or click "Help" above for more information.



##Problem 3
#Enter a part number and quantity Determine the cost per unit using the
#table below. Then calculate the total cost (quantity x unit cost). Display
#the part number, cost per unit and total cost. Note: Part number can be an
#integer but it can also be a string because you are not doing arithmetic on
#it. However, in your code if statement be sure to compare using
#consistency, that is, if item == “10” when item is a string and if item == 10
#when item is an integer.
#Part Unit Cost
#10 or 55 1.00
#99 2.00
#80 or 70 3.00
#All others 5.00

part_number = input("Please enter part number: ")
part_qty = float(input("Quantity of part: "))
part_price = float(1 if part_qty in (10, 55) else 2 if part_qty == 99 else 3 if part_qty in (80, 70) else 5)
part_totalprice = part_qty * part_price


print(f"Part number: {part_number}")
print(f"Cost per Unit: ${part_price:.2f}")
print(f"Total cost: ${part_totalprice:.2f}")



