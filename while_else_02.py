
counter = 0
while(counter < 5):
    print("menu: a.Thali, b.Chapati Sabji, c.lassi, d.paratha, q.quit")
    item = input()
    if(item == 'q'):
        break
    counter +=1
else:
    print("Limit reached!")
print("completed!")