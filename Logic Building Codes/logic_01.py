# WAP to check if an array of integers contains three increasing adjacent numbers
#     ex. [1,3,5,2,5] --> True
#         [1,1,4,2,67,5] --> False
#         [1,9,2,67,100,124,34] --> True


list1= [1,9,2,67,100,124,34]
for i in range(len(list1)-2):
    if i==len(list1):
        break
    else:
        if list1[i] < list1[i-len(list1)+1] < list1[i-len(list1)+2]:
            print(True)
        else:
            print(False)
   



