# Q9:- Given 2 fractions, find the sum of those 2 fractions.
# Take the numerator and denominator values of the fractions from the user.
num1=int(input("Enter the numretor 1="))
den1=int(input("Enter the denominator 1="))
num2=int(input("Enter the numretor 2="))
den2=int(input("Enter the denominator 2="))
total=(num1/den1)+(num2/den2)
print(round(total,2))

rn=num1*den2+num2*den1
rd=den1*den2

print('{}/{}'.format(rn,rd))