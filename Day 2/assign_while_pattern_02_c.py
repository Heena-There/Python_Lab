# 2.	Print the following patterns using loop : 
# c. 
# 1010101          
#  10101  
#   101   
#    1  


n=int(input("Enter the no: "))
print(n)
for i in range(0,n):
   # print(" "*i,"10"*(n-i-1),"1",sep="")
    print(" "*i,"1","01"*(n-i-1),sep="")