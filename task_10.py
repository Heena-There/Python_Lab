# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many
#  glasses of milk can be obtained? Assume all the inputs are provided by the user.
# Input:
# Dimensions of the milk tank
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass
# h = 3cm, r = 1cm
import math

h_t=float(input("Enter the height of tank="))
l_t=float(input("Enter the length of tank="))
b_t=float(input("Enter the breadth of tank="))

h_g=float(input("Enter the height of glass="))
r_g=float(input("Enter the radius of glass="))

Area_of_milk_tank=h_t*l_t*b_t
Area_of_glass=3.14*r_g*r_g*h_g

print("no of glasses=",math.floor(Area_of_milk_tank/Area_of_glass))
print("no of glasses=",round((Area_of_milk_tank/Area_of_glass),0))



