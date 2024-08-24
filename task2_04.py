# Problem 4: Write a menu-driven program -
# cm to ft
# km to miles
# USD to INR
# exit

# Hint
# 1 cm = 0.032ft
# 1km = 0.62
# 1 USD = 80 INR

menu=input("""Hi select an option
1. cms to ft
2. km to miles
3. USD to INR
4. Exit
""")
print("Menu=",menu)
if(menu=='1'):
    cms=int(input("Enter the centimeter="))
    print("ft value is=",cms*0.032)
elif(menu=='2'):
    km=int(input("Enter the km="))
    print("miles value is=",km*0.62)
elif(menu=='3'):
    USD=int(input("Enter the USD="))
    print("INR value is=",USD*80)
else:
    exit

