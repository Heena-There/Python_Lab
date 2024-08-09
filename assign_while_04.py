# 4.	Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
# Print average and product of all numbers.

total=0
count=0
while(1):
    num=input("Enter the number or press q: ")
    if(num=='q'):
        break
    total=total+int(num)
    count+=1
print("total",total)
print("Avg=",total/count)



