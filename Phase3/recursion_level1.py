# Foundation of Recursion (Base + Recursive Case)

# 1. Print numbers from 1 to n using recursion. 
def print1_to_n(n:int):
    if n==0:
        return 
    else:
        print1_to_n(n-1)
        print(n)

# 2. Print numbers from n down to 1 using recursion. 
def print_n_to_1(n:int):
    if n == 0:
        return
    else:
        print(n)
        print_n_to_1(n-1)

# 3. Print only even numbers from 1 to n recursively.
def print_even_1_to_n(n:int):
    if n == 0:
        return
    else:
        print_even_1_to_n(n-1)
        if n%2 == 0:
            print(n,end="")

# 4. Print only odd numbers from 1 to n recursively. 
def print_odd_1_to_n(n:int):
    if n == 0:
        return
    else:
        print_odd_1_to_n(n-1)
        if n%2 != 0:
            print(n,end=" ")

# 5. Print sum of first n natural numbers recursively.
def  sum_natural_numbers(n:int):
    if n<1:
        print("Natural numbers cannot be less than 1")
        return
    elif n == 1:
        return 1
    else:
        total = n + sum_natural_numbers(n-1)
        return total

# 6. Print factorial of a number recursively. 
def factorial_recursive(n:int):
    if n == 0 or n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)
# 7. Calculate power of a number (xⁿ) using recursion. 
def calculate_power(x:int,n:int):
    if n == 0:
        return 1
    elif n==1:
        return x
    else:
        return x*calculate_power(x,n-1)
    
# 8. Find nth Fibonacci number recursively. 
def nth_fibonacci(n:int):
    if n<=1:
        return n
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)
    
# 9. Print Fibonacci series up to n terms recursively. 
def print_fibonacci_series(n:int):
    if n<=1:
        print(n)
    else:
        print_fibonacci_series(n-1)
        print(nth_fibonacci(n-1),end=" ")    

# 10. Find sum of digits of a number recursively.
def sum_of_digits(n:int):
    dig = abs(n)
    if dig<=9:
        return dig
    else:
        return dig%10 + sum_of_digits(dig//10)
