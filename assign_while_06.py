# 6.	To display the cube of the number upto given an integer. If the given integer is 5, 
# then display cube of 1 to 4. # range(1,5)

num=int(input("Enter the no: "))
for idx in range(1,num):
    print(idx*idx*idx)
