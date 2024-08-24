# Problem 14:Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

# Input:
# H = 9 , M = 0
# Output:
# 90
# Explanation:
# The minimum angle between hour and minute hand when the time is 9 is 90 degress.


# Write code here

# Write code here
# h = int(input('Enter hours hand-'))
# m = int(input('Enter minute hand-'))

# # validate the input
# if (h < 0 or m < 0 or h > 12 or m > 60):
#     print('Wrong input')

# # Idea is to minute angle - hour agnle from clockwise from 12 hour point

# # 1 minute in minute angle make 6 degree. (60 minute -> 360 degree)
# m_angle = m*6

# # every hour point yeilds to 30degree-- 12 hours-360degree plus if minute hand moves hour hands move too
# # Every minute after hour hand take 0.5 degree movement. clockwise
# h_angle = h*30 + m*0.5

# # Take abs difference b/w them
# angle = abs(h_angle - m_angle)


# if angle>180:
#     print(360-angle)
# else:
#     print(angle)





m=int(input("Enter the minute-hand:"))
h=int(input("Enter the hour-hand:"))
m_ang=m*6
h_ang=h*30+m*0.5
ang=abs(h_ang-m_ang)
if(ang>180):
    print(360-ang)
else:
    print(ang)
