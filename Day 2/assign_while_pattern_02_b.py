# 2.	Print the following patterns using loop : 
# b. 
#     *                    
#   ***                
# ***** 
#   ***
#     * 

num=int(input("Enter the Number : "))
count=0
space=num-1
stars=1
while(count<(num//2+1)):
    print(" "*space,"*"*stars,sep="")
    stars=stars+2
    space=space-2
    count+=1

space=space+4
stars=stars-4
while(count<num):
    print(" "*space,"*"*stars,sep="")
    stars=stars-2
    space=space+2
    count+=1
    
