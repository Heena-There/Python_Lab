# Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number. 
# The numbers obtained should be printed in a space-separated sequence on a single line.

l1=[]
for i in range(1000,3001):
    if(i%2==0):
        l1.append(str(i))
print("-".join(l1))
print(l1)

# # Write code here
# L = []
# for i in range(1000,3001):
#   flag = True

#   curr = i

#   while curr > 0:
#     last = curr%10
#     if last % 2 != 0:
#       flag = False
#       break
#     curr = curr//10

#   if flag == True:
#     L.append(str(i))

# print(",".join(L))