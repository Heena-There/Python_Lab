# 10. Write a program to accept the price of a bike and display 
# the road tax and insurance to be paid according to the following criteria . 
# also display total amount to be paid.  
      
#         Cost price (in Rs)           Tax                Inssurance  
#         > 100000                     15 %                   20%  
#         > 50000 and <= 100000        10%                    8%  
#         <= 50000                     5%                     5%   

cost_price=int(input("Enter the amount: "))
if(cost_price>100000):
    print("Tax: ",int(0.15*cost_price),"Insurance: ",int(0.20*cost_price))
    total=int(0.15*cost_price + 0.20*cost_price)
    print("Total amount to be paid: ",total)
elif(cost_price>50000 and cost_price<=100000):
    print("Tax: ",int(0.10*cost_price),"Insurance: ",int(0.08*cost_price))
    total=int(0.10*cost_price + 0.08*cost_price)
    print("Total amount to be paid: ",total)
elif(cost_price<=50000):
    print("Tax: ",int(0.05*cost_price),"Insurance: ",int(0.05*cost_price))
    total=int(0.05*cost_price + 0.05*cost_price)
    print("Total amount to be paid: ",total)
else:
    print("No taxes applicable")


