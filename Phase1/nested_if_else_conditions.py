# 1. Take three sides and check if they form a valid triangle.

def is_triangle(a:float,b:float,c:float):
    if a<=0 and b<=0 and c<=0:
        # print("Invalid input")
        return False
    elif  a+b>c and a+c>b or b+c>a:
        # print(f"sides {a},{b},{c} forms a triangle")
        return True
    else:
        # print(f"sides {a},{b},{c} does not forms a triangle")
        return False

# 2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or 
# scalene.        

def type_of_triangle(a:float,b:float,c:float):
    if is_triangle(a,b,c):
        if a==b and b==c:
            print(f"sides {a},{b},{c} forms an equilateral triangle")
        elif (a==c and a!=b) or (a==b and b!=c) or (b==c and b!=a):
            print(f"sides {a},{b},{c} forms an isoscleles triangle")
        else:
            print(f"sides {a},{b},{c} forms a scalene triangle")  
    else:
        print(f"sides {a},{b},{c} does not forms a triangle")

# 3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).            

def grades(marks:int):
    if not 0<= marks <= 100:
        print("Invalid input")
        return
    if marks>40:
        print("YOU PASSES!!!")
        if marks>=90:
            print("Grade : S")
        elif marks>=80:
            print("Grade : A")
        elif marks>=70:
            print("Grade : B") 
        elif marks>=60:
            print("Grade : C")  
        elif marks>=50:
            print("Grade : D")   
        elif marks>=40:
            print("Grade : E")
    else:
        print("YOU FAilED!!!!") 
        print("Grade : F")                 

# 4. Check if one of two given numbers is a multiple of the other.         

def is_each_other_multiple(a:int,b:int):
    if a == 0 or b == 0:
        print("cannot dtermine multiple with zero")
        return
    if a%b == 0:
        print(f"{a} is a multiple of {b} ")
    elif b%a == 0:
            print(f"{b} is a multiple of {a} ")
    else:
        print(f"{a} and {b} are not multiple of each other")

# 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good 
# Evening”, or “Good Night”. 

def greeting(time:int):
    if not 0 <= time <= 23:
        print("Invalid time. Must be 0-23.")
        return
    if 12>=time >=6:
        print("Good Morning")
    elif 16>=time >12:
        print("Good Afternoon")
    elif 20>=time >4:
        print("Good Evening")
    else:
        print("Good Night")    

# 6. Check voting eligibility for a given age (18+).                

def voting_eligibilty(age:int):
    if age>=18:
        print("Congrats you are eligible to vote")
    else:
        print("You are not eligible to vote")

# 7. Take two numbers and determine whether both are even, both are odd, or one is 
# even and one is odd. 

def check_two_numbers_even_odd(a:int,b:int):
    if a%2 != 0 or b%2 != 0:
        if a%2 != 0 and b%2 != 0:
            print(f"{a} and {b} both are odd")
        elif a%2 == 0:
            print(f"{a} is even and {b} is odd")
        elif b%2 == 0:
            print(f"{b} is even and {a} is odd")
    else:
        print(f"{a} and {b} both are even")

# 8. Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

import string

def check(c:str):
    if len(c) != 1 or not c.isalpha():
        print("Invalid input. Provide a single letter.")
        return
    
    alpha_list = list(string.ascii_lowercase)
    a = alpha_list.index("m")
    if c in alpha_list[0:a+1]:
        print(f"{c} lies between a to m")
    else:    
        print(f"{c} lies between n to z ")

# 9. Take a day number (1–7) and print the corresponding day name. 

import calendar
def day_name(day:int):
    if not 1 <= day <= 7:
        raise ValueError("Days must be bewteen 1 to 7")
    days_list = calendar.day_name
    print(days_list[day-1])

# 10. Take a month number (1–12) and print the number of days in that month (ignore leap 
# years)

def number_of_days_months(month:int):
    if not 1<= month <= 12:
        raise ValueError("month must be between 1 to 12")
    elif month == 2:
        print("Days : 28")
    elif month==1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("Days : 31")
    else:
        print("Days : 30")    