# Problem 2: Write a program that take a user input of three angles and 
# will find out whether it can form a triangle or not.
# Hint - Sum of all angles is 180 and all angles are positive

first_angle=int(input("Enter the first_angle="))
second_angle=int(input("Enter the second_angle="))
third_angle=int(input("Enter the third_angle="))
summ=first_angle+second_angle+third_angle
if (summ==180):
    print("forms a triangle")
else:
    print("does not form a triangle")