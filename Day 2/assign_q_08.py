#Q8. Write a program to take marks of 3 subjects from a student. Calculate total in variable name 'total'.
#(NOTE: Don't use sum as variable name, it is built in function in python)



# a = int(input("Enter the Mark of Subject no. 1 : "))
# b = int(input("Enter the Mark of Subject no. 2 : "))
# c = int(input("Enter the Mark of Subject no. 3 : "))
total=0
for n in range(0,3):
    a = int(input("Enter the Mark of Subject: "))
    total +=a
print("Total marks Obtained: ", total)