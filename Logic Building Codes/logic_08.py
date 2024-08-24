# WAP that accepts three integers from the user and return true if two or more of them (integers ) 
# have the same rightmost digit. 
# The integers are non-negative
try:
    num1=int(input("Enter the num1= "))
    num2=int(input("Enter the num2= "))
    num3=int(input("Enter the num3= "))
    digit1=num1%10
    digit2=num2%10
    digit3=num3%10
    if(num1<0 or num2<0 or num3<0):
        print("Please enter non negative intergers only")
    elif(digit1==digit2 or digit2==digit1 or digit1==digit3):
        print(True)
    else:
        print(False)
except ValueError:
    print("Invalid input. Please enter valid integers.")

