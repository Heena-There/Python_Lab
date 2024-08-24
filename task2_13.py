# Problem 13:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. 
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

num=int(input("Enter the number="))
num1=num
summ=0
while(num>0):
    last=num%10
    last=last*last*last
    summ+=last
    num=num//10
if(summ==num1):
    print("Armstrong")
else:
    print("not armstrong")


num=int(input("Enter the no:"))
num1=num
summ=0
while(num>0):
    last=num%10
    last=last*last*last
    summ=summ+last
    num=num//10

if(summ==num1):
    print("Armstrong")
else:
    print("Not Armstrong")


num= int(input("Enter the no:"))
num1=num
summ=0
while(num>0):
    last=num%10
    last=last*last*last
    summ=summ+last
    num=num//10
if(summ==num1):
    print("armstrong")
else:
    print("not armstrong")

































