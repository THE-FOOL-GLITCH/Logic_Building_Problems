# 1. Take a number and print whether it’s positive, negative, or zero. 

def positive_negative(a:int):
    if a == 0:
        print(f"{a} is zero")
    elif a > 0 :
        print(f"{a} is positive")
    else:
        print(f"{a} is negative")        

# 2. Check if a number is even or odd       

def odd_even(a:int):
    if a%2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

# 3.   Check if a number is divisible by 5

def divisbleby5(n:int):
    if n%5 == 0:
        print(f"{n} is divisble by 5")
    else:
        print(f"{n} is not divisble by 5")   

# 4. Check if a number is divisible by both 3 and 5    

def divisible_by_3_and_5(n:int):
    if n%15 == 0:
        print(f"{n} is divisible by both 3 an 5")
    else:
        print(f"{n} is not  divisible by both 3 an 5")         

# 5. Check if a given year is a leap year.    

def is_leapyear(year:int):
    if year < 1:
        print("Invalid year input.")
        return
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

# 6. Take two numbers and print the larger one       

def larger_one(a:int,b:int):
    if a>b:
        print(f"{a} is larger than {b}")
    else:    
        print(f"{b} is larger than {a}")

# 7. take three numbers and print the largest.   

def largest_in_three(a:int,b:int,c:int):
    if a>b:
        if a>c:
            print(f"{a} is largest number among three")
        else:
            print(f"{c} is largest number among three")
    elif b>c:
        print(f"{b} is largest number among three")
    else:
        print(f"{c} is largest number among three")

# 8. Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.   

def temperature(temp:float):
    if 15 <=temp < 30:
        print("today is a warm day")
    elif 30 <= temp:
        print("today is a hot day")
    else:
        print("today is a cold day")      

# 9. take a character and check if it’s a vowel or consonant.  

def is_consonant_or_vowel(c:str):
    vowel = "aeiou"

    if c.lower() in vowel:
        print(f"{c} is vowel")
    else:
        print(f"{c} is consonant")

# 10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special 
# character

def char_type(c:str):
    if c.isnumeric():
        print(f"{c} is a digit ")
    elif not c.isalnum():
        print(f"{c} is special Character")
    elif c == c.lower():
        print(f"{c} is lowercase")      
    else:
        print(f"{c} is uppercase")
