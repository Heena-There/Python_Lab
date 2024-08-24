# 12.	Take a number from user and print sum of all odd numbers till that number.
# Ex. Enter a no : 10   
# Sum of all odd numbers till 10 : 3+5+7+9  =24

num=int(input('Enter the no: '))
summ=0
for n in range(1,num+1):
    if(n%2!=0):
        print(n)
        summ = summ + n
print("sum=",summ,sep="")