# Simple Calculator Program
# Scientific Calculator program

print("1:Addition 2:Substraction 3:Division 4:Multiplication")
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
operator=float(input("Enter the operator= "))
if(operator==1):
    print("Addition= ", num1+num2)
elif(operator==2):
    print("Substraction= ", num1-num2)
elif(operator==3):
    if(num2==0):
        print("Num is not divisible by Zero")
    else:
        print("Division= ", num1/num2)
elif(operator==4):
    print("Multiplication= ",num1*num2)
else:
    print("Invalid Operator")