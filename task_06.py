# Q6:- Write a program that will tell the number of dogs and chicken 
# are there when the user will provide the value of total heads and legs.
# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2

heads=int(input("Enter the no. of heads ="))
legs=int(input("Enter the no. of legs ="))
if heads<=legs:
    dogs=int((legs/2)-heads)
    print("No. of Dogs=",dogs)
    chicken=int(heads-dogs)
    print("No. of Chicken=",chicken)
else:
    print("Not Possible")







# count=0
# count=legs-(2*heads)
# print(count)
# dog=int(count/2)
# print(count)
# chicken=int(count-dog)
# print("dogs",dog,"chicken",chicken)
