# Q4:- Write a program to find the euclidean distance between 
# two coordinates.
# Take both the coordinates from the user as input.

x1=int(input("Enter the x1 = "))
x2=int(input("Enter the x2 = "))
y1=int(input("Enter the y1 = "))
y2=int(input("Enter the y2 = "))

distance =((x2-x1)**2 + (y2-y1)**2)**0.5
print(round(distance,2))