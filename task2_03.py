# Problem 3:Write a program that will take user input of cost price and selling price and 
# determines whether its a loss or a profit.

cost_price=int(input("Enter the cost_price="))
selling_price=int(input("Enter the selling_price="))
if(selling_price>cost_price):
    print("Profit")
elif(selling_price<cost_price):
    print("loss")
else:
    print("No loss and no gain")