# Q4. Study how format function works to print floating point values and strings . Then solve following using format function
# a. print only first 5 decimal values of 22/7 (hint: see b of Q3)
# b. print Hello string with 5 spaces on right side, 'Hello     ' ( hint: use <)
# c. print Hello string with 5 spaces on left side, '     Hello' ( hint: use <) 
# d. print Hello string with 5 '#' on left side and 5 '#' on right side, '     Hello     ' ( hint: use ^ and # as fill value)
# e. print 10 spaces (hint: give 10 as argument)

print(format(22/7, '.5f'))

str="Hello"
print("{:>10}".format(str))
print("{:<10}".format(str),"End")
print("{:#^15}".format(str))
print("Start"," "*10,"End")