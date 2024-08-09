# 8.	Ask user number of terms to be generated of a series. 
# generate numbers for the following series and find its addition 
# [9 + 99 + 999 + 9999+……..]

n=int(input("Enter the no: "))
summ=0
for idx in range(1,n+1):
    print(int("9"*idx))
    summ=summ+int("9"*idx)
print(summ)
    