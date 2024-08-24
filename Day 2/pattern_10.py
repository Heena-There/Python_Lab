row=5
star=1
space=12
count=0
while(count<row):
    print("*"*star," "*space,"*"*star,sep="")
    star+=1
    space-=2
    count+=1
# print(star-1)
# print(space+4)
# print(count<row*2+1)
star-=1
space+=2
while(count<row*2):
   print("*"*star," "*space,"*"*star,sep="")
   space+=2
   star-=1
   count+=1