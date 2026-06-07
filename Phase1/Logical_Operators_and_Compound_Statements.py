# 1. Take a character and check if it is a letter, a digit, or neither. 

def identify_char_category(c:str) -> None:
    if len(c) != 1:
        print("character must be length one")
        return
    elif c.isalpha():
        print(f"{c} is a letter")
    elif c.isdigit():
        print(f"{c} is a digit")
    else :
        print(f"{c} is neither a digit nor a letter")        
# 2. Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and 
# “FizzBuzz” if divisible by both. 

def play_fizzbuzz(n:int)->None:
    if n%15 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("fizz")
    elif n%5 == 0:
        print("buzz")        

# 3. Take three numbers and print the median value (neither maximum nor minimum). 

def find_median_of_three(a:int,b:int,c:int) -> None:
    if (b<=a<=c) or (c<=a<=b):
        print(f"{a} is median")
    elif (a<=b<=c) or (c<=b<=a):
        print(f"{b} is median")
    else:
         print(f"{c} is median")
# 4. Take 24-hour time (hours and minutes) and print whether it is AM or PM. 
def identify_am_pm(hours,minutes):
    if not (0<= hours<=23 and 0<= minutes <=59):
        print("Inavlid Input hours must be between 0 to 23 and minutes 0 to 59")
        return 
    if 0<=hours<12 :
        print("AM")
    else:
        print("PM")        
# 5. Take income and age, and check if eligible for tax (age > 18 and income > 5 L). 

def check_tax_eligibility(age:int,income:float):
    if not (age>18 and income>500000):
        print("Not eigible")
    else:
        print("Eligible")    
# 6. Take two numbers and check if both are positive and their sum is less than 100. 

def validate_positive_sum(a:float,b:float):
    if (a >0 and b>0) and a+b < 100:
        print("Both are positive and sum is smaller than 100")
    else:
        print("Any one is negative or both are or sum is greater than 100")    
# 7. Take a single digit (0–9) and print its word form (“Zero” to “Nine”). 
def digit_to_word(a:int):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    if not 0<=a<=9:
        print("invalid input number must be between 0 to 9")
        return
    else:
        print(words[a])

# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend.

def classify_day_type(day:int):
    if not 1<=day<=7:
        print("invalid input day must be between 1 to 7")
        return
    else:
        if 1<=day<=5:
            print("weekday")
        else:
            print("Weekend")    
# 9. Take electricity units consumed and calculate the bill as per slabs (using if-else). 

def calculate_electricity_bil(units:int):
    if units<0:
        print("Invalid Input units must not be negative ")
        return
    elif units<=100:
        Bill = units*5
        print(f"Total Bill : {Bill}")
    elif units<=300:
        Bill = 100*5 + (units-100)*7 
        print(f"Total Bill : {Bill}")   
    else:
        Bill =  100*5 + 200*7 + (units - 300)*10
        print(f"Total Bill : {Bill}")  
# 10. Take a password string and check basic rules (length ≥ 8 and contains at least one 
# digit). 
def validate_password_strength(password:str):
    if not len(password)>=8:
        print("too short")
        return
    has_digits = False
    for c in password:
        if c.isdigit():
            has_digits = True
            break
    if has_digits:
        print("valid") 
    else:
        print("pass is to0 weak")          