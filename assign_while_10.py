# 10.	Write a program in python to find the sum of the series [ x - x^3 + x^5 –x^7+x^9-x^11+ ......]. Go to the editor 
# Test Data : 
# Input the value of x :2 Input number of terms : 5 Expected Output : 
# The values of the series: 
# 2 
# -8 
# 32 
# -128 
# 512 
# The sum = 410 

n=int(input("Enter the num: "))
x=int(input("Enter the value of x: "))
count=1 
total=0
for idx in range(1,n+1):
    element=x**count
    if idx%2==0:
        element=-element
    print(element)
    total=total+element
    count+=2
print(total)



