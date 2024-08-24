row=5
star=5
space=0
count=0
while(count<row+1):
    print("*"*star," "*space,"*"*star,sep="")
    star-=1
    space+=2
    count+=1
# print(star+3)
# print(count)
# print(space-4)
star=star+2
space=space-4
while(count<2*row+1):
    print("*"*star," "*space,"*"*star,sep="")
    star+=1
    space-=2
    count+=1
