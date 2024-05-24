# Q8:- Given the first 2 terms of an Arithmetic Series.
# Find the Nth term of the series. Assume all inputs are provided by the user.
# Hint - an = a + (n – 1)d

first_num=int(input("Enter the first no="))
second_num=int(input("Enter the second no="))
n=int(input("Enter the num="))
d=second_num-first_num
ap=first_num+(n-1)*d
print(ap)