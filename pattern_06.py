# 2.	Print the following patterns using loop : 
# c. 
# 1010101          
#  10101  
#   101   
#    1  

row=int(input("enter the row="))
num=3
space=0
count=0
while(count<row-1):
    print(" "*space,"10"*num,"1",sep="")
    space+=1
    num-=1
    count+=1
    
