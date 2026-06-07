# 1. Take a 3-digit number and check if all digits are distinct. 

def distinct(n:int):
    s = str(abs(n))
    if len(s) != 3:
        print("Invalid digit")
        return
    
    if len(set(s)) == len(s):
        print("All digits are distinct")
    else:
        print("All digits afre not distinct")    

# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or 
# neither. 
def analyze_middle_digit(n: int) -> None:
    s = str(abs(n))
    if len(s) != 3:
        print("Invalid input: Must be a 3-digit number.")
        return
    
    # OPTIMIZATION: Convert once, store in variables.
    d1, d2, d3 = int(s[0]), int(s[1]), int(s[2])

    if d2 > d1 and d2 > d3:
        print(f"Middle digit {d2} is the LARGEST.")
    elif d2 < d1 and d2 < d3:
        print(f"Middle digit {d2} is the SMALLEST.")
    elif d2 == d1 == d3:
        print(f"All digits are equal ({d2}).")
    elif d2 == d1 or d2 == d3:
        print(f"Middle digit {d2} is TIED with another digit.")
    else:
        # This correctly catches cases like 1-2-3 or 3-2-1
        print(f"Middle digit {d2} is NEITHER largest nor smallest.")


# 3. Take a 4-digit number and check if the first and last digits are equal. 
def has_equal_ends(n:int):
    s = str(abs(n))
    if len(s) != 4:
        print("Invalid input: Must be a 4-digit number.")
        return
    
    first,last = int(s[0]),int(s[3])
    if first == last :
        print("First and last digits are equal")
    else:
        print("first and last digits are not equal")    
# 4. Check whether a given integer is single-digit, double-digit, or multi-digit. 
def classify_digit_count(n:int):
    if n == 0:
        print("n is zero")   
        return
    a = abs(n) 
    if 0<a<10:
        print("N is a single digit number")
    elif 10<= a <100:
        print("n is double digit number")
    else:
        print("n is multi digit number")    
    


# 5. Check if a number is a multiple of 7 or ends with 7. 

def check_seven_property(n:int):
    num = abs(n)
    if num%7 == 0:
        print("num is divisible by 7")
    if num%10 == 7:
        print("num ends with 7")    

# 6. Take coordinates (x, y) and determine which quadrant the point lies in.
def get_quadrant_location(x: float, y: float) -> None:
    if x == 0 and y == 0:
        print("Point is at the Origin")
    elif x == 0:
        # If x is 0, the point must be on the vertical line
        print("Point is on the Y-axis")
    elif y == 0:
        # If y is 0, the point must be on the horizontal line
        print("Point is on the X-axis")
    elif x > 0 and y > 0:
        print("Quadrant 1")
    elif x < 0 and y > 0:
        print("Quadrant 2")
    elif x < 0 and y < 0:
        print("Quadrant 3")
    else:
        # Since all other 6 cases are checked, it must be Q4
        print("Quadrant 4")
# 7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
def is_valid_currency_combination(amount:int) -> None:
    if amount<= 0:
        print("Invalid amount")
        return
    if amount%100 != 0:
        print("amount cannot be divided")
        
# 8. Check if a number lies within the range [100, 999].

def is_three_digit_range(n:int):
    if n in range(100,1000):
        print("True")
    else:
        print(False)    
# 9. Take two angles of a triangle and compute the third angle. 
def calculate_third_angle(angle1:int,angle2:int) -> None:
    if angle1>0 and angle2>0:
        if (angle1 + angle2) < 180:
            angle3 = 180 - (angle1 + angle2)
            print(angle3)
        else:
            print("invalid input")    
    else:
        print("Invalid input angles cannot be negative")

# 10. Check whether a number is a perfect square (without using the square root function).
def is_perfect_square(n:int):
    if n<0:
        print("no roots exits of negative number")
        return
    i = 0
    while i*i<=n:
        if i*i == n:
            break
        i += 1

    if i*i == n:
        print("N is a perfect square")
    else:
        print("n is not a perfect square")            