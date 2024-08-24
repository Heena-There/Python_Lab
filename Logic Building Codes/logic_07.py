# WAP to print numbers between 1 to 100 which are divisible by 3, 5 and by both
# ( total 3 list of numbers to be printed)

l3=[]
l5=[]
l35=[]
for i in range(1,100):
    if(i%3==0):
        l3.append(i)
    if(i%5==0):
        l5.append(i)
    if(i%3==0 and i%5==0):
        l35.append(i)
print(l3)
print(l5)
print(l35)