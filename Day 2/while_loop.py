#Wap to print "*" to print 5 times on same line using while loop
idx = 0
while idx < 5:
    print("*",end=" ")
    idx+=1 #there is no ++
print("*"*5)

num=int(input("Enter the num:"))
for i in range(1,num+1):
    print("*",end="")
