#Problem4

item_line = 0
quantity_line = 1
price_line = 2
extprice_sum = 0
order_sum = 0
with open('item_info.txt', 'r') as doc:
    doc_content = doc.readlines()
    doc_length = len(doc_content)
    while item_line < doc_length:
        item = doc_content[item_line].strip()
        quantity = float(doc_content[quantity_line].strip())
        price = doc_content[price_line].strip()
        extprice = float(quantity) * float(price)
        item_line += 3
        quantity_line += 3
        price_line += 3
        extprice_sum += extprice
        order_sum += quantity
        if item=="":
            break
        print (f"Item: {item} Quantity: {quantity} Total price: {extprice:.2f}")
average_order = float(extprice_sum/order_sum)
print(f"Total Extended Price: ${extprice_sum:.2f} Total Orders: {order_sum:.0f} Average Order Price: ${average_order:.2f}")
        
