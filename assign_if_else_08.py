# 8.	Write a program to check whether the last digit of a 
# number( entered by user ) is divisible by 3 or not.

num = int(input("Enter the no : "))
print(num)
if(num%10%3==0):
    print("No. is divisible by 3")
else:
    print("No. is not divisible by 3")


