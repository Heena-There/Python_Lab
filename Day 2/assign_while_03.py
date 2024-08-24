
# 3.	Write a program to find greatest common divisor (GCD) or 
# highest common factor (HCF) of given two numbers.

a=int(input("Enter the no.- "))
b=int(input("Enter the no.- "))
if(a>b):
    small=b
else:
    small=a
s=0
for n in range(1,small+1):
    if(a%n==0 and b%n==0):
        s=n
print(s)
