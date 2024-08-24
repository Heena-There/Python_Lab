# # Simple Calculator Program
# # Scientific Calculator program
print("1.Addition,2.Subtraction,3.Multiplication,4.Division")
num1=float(input("Enter the num1="))
num2=float(input("Enter the num2="))
# print("1.Addition,2.Subtraction,3.Multiplication,4.Division")
Operator=float(input("Enter the Operator:"))
if(Operator==1):
    print("Addition=",num1+num2)
elif(Operator==2):
    print("Subtraction=",num1-num2)
elif(Operator==3):
     print("Multiplication=",num1*num2)
elif(Operator==4):
    if(num2==0):
        print("Given no. is not divisible by Zero")
    else:
          print("Division",num1/num2)
else:
    print("Invalid Operator")
# print("1.Add,2.subs,3.div,4.mult")

# int1=float(input("Enter 1 number"))
# int2=float(input("Enter 2 number"))

# operator=float(input("Enter Choice"))
# if operator==1:
#     print("add",int1+int2)
# if operator==2:
#         print("sub",int1-int2)
# if operator==3:
#          if int2==0:
#               print("cant divide by zero")
#          else:
#               print("divi",int1/int2)
# if operator==4:
#      print("mutli",int1*int2)
        
