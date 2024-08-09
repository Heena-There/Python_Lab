# 7.	Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :  
#              Unit                                    Price    
# First 100 units                                       no charge  
# Next 100 units                                        Rs 5 per unit  
# After 200 units                                       Rs 10 per unit  
# (For example if input unit is 350 than total bill amount is Rs2000) 

units = int(input("Enter the units: "))
print(units)
if(units<=100):
    print("No Charge")
elif(units>100 and units<=200):
    print("Charges : ",5*units)
else:
    print("Charges: ",10*units)