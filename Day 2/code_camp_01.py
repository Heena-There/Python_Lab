# Program - Find the sum of a 3 digit number entered by the user

number=int(input("Enter the number="))
print(number)
counter=0
summ=0
# for i in range(len(number)):
while number!=0:
    num1=number%10
    summ+=num1
    number=number//10
    
print(summ)