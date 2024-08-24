# 2. accept amount from user and find the minimum number notes required to get the amount amount =512  
# Notes: 2000,500,100,50,10,5,2,1  

# 500-1 note  
# 10  - 1 note  
# 2-  1 coin  

# amount=20550
# 2000 – 10 note
# 500 – 1 note 
# 50 -1 note 

# amount = int(input("Enter an amount: "))
# #we are storing all notes in list
# notes = [2000,500,100,50,10,5,2,1]  
# #empty dictionary
# num_notes = {}    
# for note in notes:
#     # returns no. of particular notes by traversing the list index-wise
#     num_notes[note] = amount//note
#     # returns the remaining amount
#     amount=amount%note
# # reading the key-value pairs in dict where note and its count is stored
# for note, count in num_notes.items():
#     # if the count of notes is non-zero, display it
#     if count>0:
#         #printing the note and its count from dict in the given format
#         print(note,' - ',count, ' note')


# amount = int(input("Enter the amount : "))
# notes = [2000,500,100,50,10,5,2,1]
# for note in notes:
#     if(amount>note):
#         count = amount//note
#         amount=amount-note*count
#         print(note,"--",count)



# amt=int(input("Enter the amount:"))
# notes=[2000,500,200,100,50,20,10,5,2,1]
# for note in notes:
#     if (amt>note):
#         count=amt//note
#         amt=amt-note*count
#         print(note,"--",count)



cash=int(input("Enter the cash:"))
lists=[2000,500,100,200,50,20,10,1,5]
for note in lists:
    if cash>note:
        count=cash//note
        cash=cash-note*count
        print(note,"--",count)




































