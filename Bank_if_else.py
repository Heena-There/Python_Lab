income = int(input("Enter the Customer Income : "))
print(income)
if(income>100000):
    print("Platinum")
elif(50000<income<=100000):
    print("Gold")
elif(25000<income<50000):
    print("Silver")
else:
    print("Bronze")