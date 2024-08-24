# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - 
# HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

CTC=int(input("Enter the salary="))
if (CTC<500000):
    salary=(CTC*0.10+CTC*0.05+CTC*0.03)
    salary=(CTC*0.82)
    print("Salary=",round(salary//12,2))
elif(CTC<1000000):
    salary=(CTC*0.10+CTC*0.05+CTC*0.03+CTC*0.10)
    salary=(CTC*0.72)
    print("Salary=",round(salary//12,2))
elif(CTC<2000000):
    salary=(CTC*0.10+CTC*0.05+CTC*0.03+CTC*0.20)
    salary=(CTC*0.62)
    print("Salary=",round(salary//12,2))
else:
    salary=(CTC*0.10+CTC*0.05+CTC*0.03+CTC*0.30)
    salary=(CTC*0.52)
    print("Salary=",round(salary//12,2))
print("Salary",round(salary//12,2))