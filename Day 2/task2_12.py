# Problem 12:Write a program to print whether a given number is a prime number or not

num=int(input("Enter the no="))
for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break
        i+=1
else:
    print("Prime")

# Problem 13:Write a program to print the prime number between the given range.
num=int(input("Enter the no:"))
l1=[]
for i in range(2,num):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
            l1.append(i)
print(l1)





