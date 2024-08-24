# 9.	Write a program in python to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]. Go to the editor 
# Test Data : 
# Input the value of x :3 Input number of terms : 5 Expected Output : 
# The sum is : 16.375000 
import math
n=int(input("Enter the number: "))
x=int(input("Enter the value of x: "))
total=0
for idx in range(0,n):
    # fact=fact*idx
    element=x**idx/math.factorial(idx)
    print(element)
    total+=element
print(total)