# 2.	Print the following patterns using loop : 
# b. 
#     *                    
#   ***                
# ***** 
#   ***
#     * 

num=int(input("enter the row:"))   #5
star=1
space=num-1
count=0
while(count<num//2+1):
    print(" "*space,"*"*star,sep="")
    space-=2
    star+=2
    count+=1
# print(star)
# print(space)
# print(count)

star-=4
space+=4
while(count<num):
    print(" "*space,"*"*star,sep="")
    space+=2
    star-=2
    count+=1
