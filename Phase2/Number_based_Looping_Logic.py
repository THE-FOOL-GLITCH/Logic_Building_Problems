# 1. Count the number of digits in a given number. 

def count_digits(n:int):
    if n == 0:
        print(1)
        return
    count = 0
    temp = abs(n)
    while temp>0:
        count += 1
        temp = temp//10
    print(count)
        

# 2. Print the reverse of a given number. 

def reverse_number(n:int)->int:
    reversed_num = 0
    temp = abs(n)
    while temp>0:
        dig = temp%10
        reversed_num = (reversed_num*10) + dig
        temp //= 10
    return -reversed_num if n < 0 else reversed_num

# 3. Check if a number is a palindrome. 
def is_palindrome(n:int)->bool:
    if n<0:
        return False
    return n == reverse_number(n)
# 4. Find the sum of digits of a number. 
def get_digit_sum(n:int)->int:
    temp = abs(n)
    total = 0
    while temp>0:
        dig = temp%10
        total += dig
        temp //= 10
    return total  
# 5. Check if a number is an Armstrong number.
 
def is_armstrong(n: int) -> bool:
    # Armstrong numbers are technically defined for positive integers
    if n < 0:
        return False
        
    original_num = n
    k = len(str(n))
    total = 0
    temp = n
    
    while temp > 0:
        dig = temp % 10
        total += dig ** k
        temp //= 10
        
    return total == original_num
# 6. Check if a number is a perfect number. 

def is_perfect_number(n:int):
    if n<0:
        return False
    total = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            total+=i
    return total == n        
# 7. Print all prime numbers between 1 and 100. 

def print_primes_1_to_100(n=100):
    if n<1:
        print("Prime numbers are always greater than 1 ")
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i,end=" ")
            
# 8. Check if a number is prime or not. 

def check_prime(n:int):
    if n<=1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2,int((n**0.5))+1):
            if n%i == 0:
                return True
        else:
            return True    

# 9. Print Fibonacci series up to n terms. 

def print_fibonacci_series(n: int) -> None:
    if n <= 0:
        print("Please enter a positive integer.")
        return
        
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        # The simultaneous swap pattern:
        a, b = b, a + b
    print()

# Test call for 9 terms
# Output: 0 1 1 2 3 5 8 13 21
# 10. Print sum of first n terms of Fibonacci series.

def sum_fibonacci_series(n:int) -> int:
    if n <= 0:
        return 0
    a,b = 0,1
    total = 0
    for _ in range(n):
        total += a
        a,b = b,a+b
    return total    

