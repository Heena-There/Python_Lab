# Problem 8: Take a user input as integer N. Find out the sum from 1 to N. 
# If any number if divisible by 5, then skip that number. And 
# if the sum is greater than 300, don't need to calculate the sum further more. 
# Print the final result. 
# And don't use for loop to solve this problem.

num=int(input("Enter the no:"))
summ=0
i=1
while(i<num+1):
    if(i%5==0):
        i+=1
        continue
    summ+=i
    if(summ>300):
        summ-=i
        break
    i+=1
print(summ)