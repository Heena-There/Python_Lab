# 1.	Accept 10 integers from user  and print their average value on the screen 

total=0
counter=0
for n in range(10):
    num=int(input("Enter the no: "))
    total=total+num
    counter+=1
print(total)    
avg=total/counter
print(avg)