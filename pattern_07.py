# 2.	Print the following patterns using loop :
# d.
# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5

row=int(input("Enter the row="))
for i in range(0,row+1):
    for j in range(1,i+1):
        print(j,end='')
        j+=1
    print()


row=5
num=65
for i in range(0,row):
    for j in range(0,i+1):
        ch=chr(num)
        print(ch,end=" ")
    num+=1
    print()

row=5
star=5
count=0
while(count<row):
    print("*"*star,sep="")
    star-=1
    count+=1