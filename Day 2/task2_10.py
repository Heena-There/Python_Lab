# Problem 9: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# l1=[]
# for i in range(2000,3201):
#     if(i%7==0 and i%5 !=0):
#         l1.append(str(i))
# print(",".join(l1))
# print(l1)








list1=[]
for i in range(7,77):
    if (i%7==0 and i%5!=0):
        list1.append(str(i))
print(".".join(list1))
print(list1)











