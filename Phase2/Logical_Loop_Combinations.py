# 1. Print all numbers whose sum of digits is even (1–100). 


def print_even_digit_sum_numbers(n=100)->None:
    for i in range(1,n+1):
        temp = i
        dig_sum = 0
        while temp>0:
            dig = temp%10
            dig_sum += dig
            temp //= 10
        if dig_sum%2 == 0:
            print(i)     
        
# 2. Count how many numbers between 1–500 are divisible by 7 but not by 5.

def count_divisible_numbers(n=500):
    count = 0
    for i in range(1,n+1):
        if i%7 == 0 and i%5 != 0:
            count += 1
    print(count)
                
# 3. Print all numbers that are palindromes between 1–500. 

def print_palindromic_numbers(n=500):
    from Number_based_Looping_Logic import is_palindrome
    for i in range(1,n+1):
        if is_palindrome(i):
            print(i,end=" ")

# 4. Print numbers between 1–100 whose digits add up to a multiple of 3.

def print_digit_sum_multiples_of_three(n=100):
    for i in range(3,n+1):
        temp = i
        dig_sum = 0
        while temp>0:
            dig = temp%10 
            dig_sum += dig
            temp //= 10
        if dig_sum%3 == 0:
            print(i)    



# 5. Find the smallest and largest digit in a given number. 

def find_min_max_digits(n:int):
    temp = abs(n)
    imin = float('inf')
    imax = float('-inf')
    while temp>0:
        dig = temp%10 
        imin = min(dig,imin)
        imax = max(dig,imax)
        temp //= 10
    return imax,imin

# 6. Print all numbers from 1–n whose binary representation has an even number of 1s. 

def print_even_binary_ones(n:int):
    for i in range(1,n+1):
        count = 0
        temp = i
        while temp>0:
            if temp & 1:
                count += 1
            temp >>= 1
        if (count & 1) == 0:
            print(i,end="") 
    print()               

# 7. Print a pattern where each row i prints i*i. 

def print_square_sequence(n:int):
    for i in range(1,n+1):
        print(i*i)
        
# 8. Print factorial of each number from 1 to n. 

def print_factorial_sequence(n:int):
    from basic_looping import factorial
    for i in range(1,n+1):
        print(factorial(i))
    print()   
 

# 9. Print the sum of all odd digits and even digits separately in a number.

def sum_even_odd_digits(n:int):
    temp = abs(n)
    even_sum = 0
    odd_sum = 0 
    while temp>0:
        dig = temp%10
        if dig%2 == 0:
            even_sum += dig
        else:
            odd_sum += dig
        temp //=10
      
# 10. Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print 
# the sum of all non-zero numbers entered. 

def interactive_sum_non_zero(n=5):
    total = 0
    for i in range(n):
        dig = int(input("Enter your number :"))
        if dig==0:
            continue
        else:
            total += dig
    print(total)        
          