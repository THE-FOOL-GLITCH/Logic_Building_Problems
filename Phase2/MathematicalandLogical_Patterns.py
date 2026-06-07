# 1. Print the squares of numbers from 1 to n. 

def print_squares(n: int) -> None:
    # Fail fast: validate input before running loops
    if n < 1:
        print("Please enter an integer greater than or equal to 1.")
        return
        
    for i in range(1, n + 1):
        print(i * i, end=" ")
    print()  # Clear line at the end

# 2. Print cubes of numbers from 1 to n. 

def print_cubes(n:int)->None:
    if n<1:
        print("Please enter an integer greater than or equal to 1.")
        return
    
    for i in range(1,n+1):
        print(i**3,end=" ")
    print()    
        
# 3. Print all numbers between a and b divisible by 7.

def print_divisible_by_seven(a:int,b:int): 
    start = -(-a//7) * 7 
    for i in range(start,b+1,7):
        print(i,end=" ")
    print()
# 4. Find HCF (GCD) of two numbers using loops. 

def find_hcf(a:int,b:int):
    for i in range(min(a,b),0,-1):
        if a%i ==0 and b%i==0:
            return i
# 5. Find LCM of two numbers using loops. 
def find_lcm(a:int,b:int):
    lcm = abs(a*b)//find_hcf(a,b)
    return lcm
# 6. Print all factors of a given number. 
def print_factors(n: int) -> None:
    n = abs(n)
    if n == 0:
        print("0 has infinite factors.")
        return

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            print(i, end=" ")
            # If the co-factor is different, print it too!
            if i != n // i:
                print(n // i, end=" ")
    print()
# 7. Find the sum of all factors of a number. 

def sum_factors(n:int):
    n = abs(n)
    if n == 0:
        return 0
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            # If the co-factor is different, print it too!
            if i != n // i:
                total += n//i
    print(total)
# 8. Check if a number is a strong number (sum of factorials of digits = number). 

def is_strong_number(n:int):
    from basic_looping import factorial
    if n == 0:
        return False
    temp = abs(n)
    total = 0
    while temp>0:
        dig = temp%10
        total += factorial(dig)
        temp //= 10
    return total == abs(n)    



# 9. Print first n terms of an arithmetic progression (a, d)

def print_ap(n:int,a:int,d:int):
    if n < 1:
        print("Invalid input please enter a positive integer more than 1")
        return
    b = a
    while n > 0:
        print(b,end=" ")
        b += d
        n -= 1
    print()    

# 10. Print first n terms of a geometric progression (a, r). 

def print_gp(n:int,a:int,r:int):
    if n < 1:
        print("Invalid input please enter a positive integer greater than or equal to 1")
        return
    b = a
    while n > 0:
        print(b,end=" ")
        b *= r
        n -= 1
    print()    

