# 3.	Modify the above question Q1 to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

Total_attendance = int(input("Enter the Total attendance : "))
Total_Lecture = int(input("Enter the Total Lecture: "))
print(Total_attendance,Total_Lecture)
Attendance = (Total_attendance/Total_Lecture) *100
if(Attendance<=75):
        medical_cause=input("Enter Medical Cause Y or N: ")
        if(medical_cause=="Y"):
              print("Allowed to Sit in exam")
        else:
              print("Allowed not to Sit in exam")
else:
    print("Allowed to Sit in exam")