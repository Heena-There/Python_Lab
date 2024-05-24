# Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
fnum=int(input("Enter the first num= "))
snum=int(input("Enter the first num= "))
temp=0
temp=fnum
fnum=snum
snum=temp
print("First No: ",fnum,"Second No: ",snum)

#tuple logic for swapping no.
(fnum,snum)=(snum,fnum)
print(fnum,snum)