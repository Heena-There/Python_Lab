# WAP to convert input number of seconds to HH:MM:SS.
def convert_secs_to_HMS(seconds):
    hour=seconds//3600
    min=(seconds % 3600)//60
    sec=seconds%60

    return f"{hour:02}:{min:02}:{sec:02}"
try:
    total_sec=int(input("Enter the total no of secs= "))
    if(total_sec<0):
        print("Enter valid no of secs")
    else:
        time_string=convert_secs_to_HMS(total_sec)
        print(time_string)
except ValueError:
    print("Invalid input. Please enter valid integers.")





    