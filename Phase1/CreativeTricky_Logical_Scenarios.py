# 1. Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or on the 
# origin. 
def check_coordinate_location(x:float,y:float) -> None:
    if x == 0 and y ==0:
        print("Point exists on origin")
    elif x == 0:
        print("Point exists on Y axis")    
    elif y == 0:
        print("Point exists on X axis")  
    else:
        print("The point is in one of the four quadrants (not on an axis).")      

# 2. Take three numbers and check if they can form a Pythagorean triplet.

def is_pythagorean_triplet(x:int,y:int,z:int):
    if  (x<=0 or y<=0 or z<=0) :
        print("Triangle sides cannot be zero")         
        return
    sides = sorted([x,y,z])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print(f"sides {x},{y} and {z} form pythogoras triplets")
    else:
        print(f"sides {x},{y} and {z} does not  form pythogoras triplets")

# 3. Take day and month and check if it forms a valid calendar date (ignoring leap years). 

def is_valid_calendar_date(day: int, month: int) -> None:
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1. First, check if the month is valid to prevent an IndexError
    if month < 1 or month > 12:
        print("Invalid Month: Must be between 1 and 12.")
        return False
    
    # 2. Now it's safe to check the days using the lookup table
    if 1 <= day <= days_in_month[month]:
        print(f"Success: {day}/{month} is a valid date.")
        return True
    else:
        print(f"Error: Month {month} only has {days_in_month[month]} days.")
        return False

# 4. Take time (hours and minutes) and print the smaller angle between the hour and 
# minute hands. 

def calculate_clock_angle(hours:int,minutes:int) -> None:
    if not (11>=hours>=0 and 59>=minutes>=0):
        print("Invalid Input hours must be between 0 to 11 and minutes must be between 0 to 59")
        return
    else:
        Angle = abs(hours*30 + minutes*0.5 - minutes*6)
        if Angle > 180:
            print(f"Angle : {360-Angle}")
        else:
            print(f"Angle : {Angle}")

# 5. Take three numbers and check if they are in arithmetic progression. 

def is_arithmetic_progression(a:float,b:float,c:float):
    if (a-b) == (b-c):
        print(f"{a},{b},{c} form an arithmetic progression")
    else:    
        print(f"{a},{b},{c} doesn't form an arithmetic progression")
# 6. Take three numbers and check if they are in geometric progression.

def  is_geometric_progression(a:float,b:float,c:float)->None:
    if b**2 == a*c:
        print("Is valid geometric expression")
    else:
        print("Does not form geometric expression")    

# 7. Take a 3-digit number and check if the sum of the first and last digit equals the middle 
# digit. 

def check_digit_relation(num:int)->None:
    s = str(abs(num))
    if len(s) != 3:
        print("Invalid input, Num must have three digits")
    else:
        n1,n2,n3 = int(s[0]),int(s[1]),int(s[2])
        if n1 + n3 == n2:
            print("sum of first and last digit equals to middle digit ")
        else:
            print("sum of first and last digit does not equals to middle digit")

# 8. Take an integer (1–9999) and check if the sum of its digits is greater than the product 
# of its digits. 

def compare_digit_sum_and_produc(n:int):
    if n<1 or n>9999:
        print("Invalid input num must be between 1 to 9999")
        return
    d_sum = 0
    d_product = 1
    temp_num = n
    while temp_num>0:
        digit = temp_num%10
        d_sum += digit
        d_product *= digit
        temp_num//=10

    if d_sum > d_product:
        print("Sum is greater than product")
    else:
        print("Sum is not greater than product ")       
# 9. Take two dates (day and month) and determine which one comes first in the 
# calendar. 
def compare_dates(month1:int,month2:int,day1:int,day2:int):
    if is_valid_calendar_date(month1,day1) and is_valid_calendar_date(month2,day2):
        if month1>month2:
            print("date 2 is earlier")
        elif month1<month2:
            print("date 1 is earlier")
        else:
            if day1 > day2:
                print("date 2 is earlier")
            else:
                print("date 1 is earlier ")
    else:
        print("Invalid dates")            
            
# 10. Take a year and print the corresponding century (e.g., “19th century”, “20th century”)

def get_century_name(year: int) -> None:
    if year < 1:
        print("Error: Year must be 1 or greater.")
        return

    # Correct Mathematical Formula
    century = (year - 1) // 100 + 1
    
    # Logic for Suffixes (Handling the 11th, 12th, 13th exceptions)
    if 11 <= (century % 100) <= 13:
        suffix = "th"
    else:
        # Use a dictionary for cleaner lookups
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        suffix = suffixes.get(century % 10, "th")
    
    print(f"{year} belongs to the {century}{suffix} Century.")
