# Q5. We can use ord() to print ASCII value of single character 
# and chr() to convert given ASCII value to character. 
# a. find ASCII of characters'a' , 'A' , 'z' , 'Z' using ord() one by one
# b. find ASCII of characters '0', '9', ' ', "\n" , "\t" using ord() one by one
# c. Find characters for ASCII values 35, 67, 50, 99
# d. Where ASCII value begin for lower case characters where it ends? also find 
# same for digits and upper case characters

print(ord("a"))
print(ord("A"))
print(ord("z"))
print(ord("Z"))

print(ord("0"))
print(ord("9"))
print(ord(" "))
print(ord("\n"))
print(ord("\t"))

print(chr(35))
print(chr(67))
print(chr(50))
print(chr(99))

print(ord("A"))


for n in range(65,90):
    num=int(input("Enter the digit: "))
    print("Uppercase: ",chr(num))
for n in range(99,127):
    num=int(input("Enter the digit: "))
    print("Lowercase: ",chr(num))
# num=int(input("Enter the digit: "))
# if(range(ord("A"),ord("Z"))):
#     print("Uppercase")
# elif(range(ord("a"),ord("b"))):
#     print("Lowercase")
# else:
#     print("End")


