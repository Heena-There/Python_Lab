# A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
# Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
# Is student is allowed to sit in exam or not. 

Total_attendance = int(input("Enter the Total attendance : "))
Total_Lecture = int(input("Enter the Total Lecture: "))
print(Total_attendance,Total_Lecture)
Attendance = (Total_attendance/Total_Lecture) *100
print(Attendance)
if(Attendance >=75):
    print("Allowed to Sit in exam")
else:
    print("Not Allowed to Sit in exam")




print("--------------------------------------------------------------------------")
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
# Take following input from user Number of classes held Number of classes attended. And print percentage of class 
# attended  
# Is student is allowed to sit in exam or not.

tot_attend=int(input("Enter the attendance: "))
tot_lec=int(input("Enter the total lecture: "))
present=(tot_attend/tot_lec)*100
print(present)
if(present>75):
    print("Candidate is allowed to attain the exam")
else:
    print("not allowed")

















