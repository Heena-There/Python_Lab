# 5.	Given a number count the total number of digits in a number and 
# also find sum of digits of the number.

num=int(input("Enter the num= "))
total=0
count=0
while(num>0):
# for idx in range(1,num):
    rem=num%10
    total=total+rem
    num=num//10
    count+=1
print("count=",count)
print(total)