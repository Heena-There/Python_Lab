# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5

num=int(input("Enter the number="))
print(num)
for i in range(1,num):
    num=num*i
print(num)