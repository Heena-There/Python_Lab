tot_lect = int(input("Enter total lectures: "))
att_lect = int(input("Enter attended lectures: "))
print(att_lect,tot_lect)
per_att = att_lect/tot_lect * 100

if(per_att>75):
    print("Allowed for exam")
elif(per_att>50):
    print("Allowed with 40% reduction in marks")
else:
    print("Not allowed")   