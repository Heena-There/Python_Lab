# 3.	Modify the above question Q1 to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.  
# 4.	A school has following rules for grading system:  
# a.	Below 25 - F  
# b.	25 to 45 - E  
# c.	45 to 50 - D  
# d.	50 to 60 - C  
# e.	60 to 80 - B  
# f.	Above 80 - A  
# Ask user to enter marks and print the corresponding grade.

Marks = int(input("Enter the Marks : "))
print(Marks)
if(Marks<=25):
    print("F")
elif(Marks>25 and Marks<=45):
    print("E")
elif(Marks>45 and Marks<=50):
    print("D")
elif(Marks>50 and Marks<=60):
    print("C")
elif(Marks>60 and Marks<=80):
    print("B")
else:
    print("A")