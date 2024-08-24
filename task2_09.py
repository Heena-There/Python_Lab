# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. 
# Display the sum and average of all the numbers.
# summ=0
# count=0
# while True:
#     num=int(input("Enter the num="))
#     if(num==0):
#         print("quit")
#         break
#     summ=summ+num
#     count=count+1
#     avg=float(summ//count)
# print("summ=",summ)
# print("count=",count)
# print("avg=",avg)




summ=0
count=0
while True:
    num=int(input("Enter the no:"))
    if(num==0):
        break
    summ=summ+num
    count=count+1
    average=summ//count
print(summ)
print(count)
print(average)