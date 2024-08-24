# 6.	Accept number from user and check whether it is divisible by 5 and 11 if divisible then display appropriate message.  


num = int(input("Enter the number : "))
print(num)
if(num % 5 ==0 and num % 11 ==0):
    print("No. is divisible by 5 & 11")
else:
    print("No. is not divisible by 5 & 11")