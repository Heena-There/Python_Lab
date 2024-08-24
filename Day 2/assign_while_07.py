# 7.	Accept 20 numbers from user and display sum of only even numbers. 
l1=[]
total=0
for idx in range(0,20):
    num=int(input("Enter the num: "))
    l1.append(num)
    if(num%2==0):
        total=total+num
print("l1=",l1)
l2=[e for e in l1 if e%2==0]
print("l2=",l2)
print(total)