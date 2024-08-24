#Diamond Pattern

num = int(input("Enter the no. :"))
count=0
stars=1
spaces=num//2
while(count < (num//2 +1)):
    print(" "*spaces,"*"*stars,sep="")
    spaces=spaces-1
    stars=stars+2
    count+=1
stars=num-2
spaces=1
while(count>1):
    print(" "*spaces,"*"*stars,sep="")
    spaces=spaces+1
    stars=stars-2
    count-=1


