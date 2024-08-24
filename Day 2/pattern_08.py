# Hollow Inverted Half Pyramid:
# *****
# *   *
# *  *
# * *
# **

row=5
star=5
space=0
count=0
while(count<row//2-1):
    print("*"*star,sep="")
    count+=1
star=1
space=3
while(count<row-1):
    print("*"*star," "*space,"*"*star,sep="")
    space-=1
    count+=1
