# marks=[86,99,100,90,45,70,68,79]
# for m in marks:
#     print(m)
#     if m <=50:
#         print("fail")
#         break
# else:
#     print("All Pass!")

marks=[86,99,100,90,45,70,68,79]
for m in marks:
    if m <=50:
        print(m,"fail")
        continue
    else:
        print(m,"All Pass!")
