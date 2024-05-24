# Q5:- Write a program to find the simple interest when 
# the value of principle,rate of interest and time period is 
# provided by the user.
p=int(input("Enter the principle = "))
r=float(input("Enter the Rate of Interest = "))
t=float(input("Enter the time span = "))

si=(p*t*r)/100
print(si)

print("Amount=",si+p)