#Q7. Write a Python program to input cost price and selling price of a product and check profit or loss.

costPrice = int(input("Enter the cost price of product: "))
sellPrice = int(input("Enter the selling price of product: "))

if sellPrice > costPrice:
	print("Seller made profit: ",(sellPrice - costPrice))
else:
	print("Seller is in loss: ",(sellPrice - costPrice))
