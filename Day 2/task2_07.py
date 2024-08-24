# Problem 7 - Reverse a given integer number.

num=int(input("Enter the number="))
print(num)
rem=0
while(num>0):
    last=num%10
    rem=rem*10+last
    num=num//10
print(rem)