#  Number-based Recursive Thinking 

# 1. Count the number of digits in a number recursively. 
def count_digits(n:int):
    if abs(n)<10:
        return 1
    else:
        total = 1 + count_digits(abs(n)//10)
        return total
    
# 2. Reverse a number recursively. 
def reverse_number(n:int):
    sign = -1 if n<0 else 1

    def reverse_engine(num:int,current_reverse:int):
        if n==0:
            return current_reverse
        
        last_dig = num%10
        updated_reverse = current_reverse*10 + last_dig
        return sign*reverse_engine(abs(n),0)


# 3. Check if a number is a palindrome using recursion. 
def is_palindrome(n:int):
    val = abs(n)
    return val == reverse_number(val)

# 4. Find product of digits of a number recursively. 
def product_of_digits(n:int):
    val = abs(n)
    if val < 10:
        return val
    else:
        product = (val%10) * product_of_digits(val//10)

# 5. Find GCD (HCF) of two numbers using Euclid’s algorithm recursively. 
def GCD(a:int,b:int):
    if b == 0:
        return abs(a)
    else:
        return GCD(b,a%b)
    
# 6. Convert a number to binary recursively. 
def to_binary(n:int):
    if n <1:
        return str(n)
    else:
        return to_binary(n//2) + str(n%2)
    
# 7. Print digits of a number in words recursively (e.g., 123 → “one two three”).
def print_words(n:int):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    if n == 0:
        return words[0]
    def get_words(val:int):
        if val == 0:
            return ""
        else:
            return get_words(val//10) + " " + words[val%10]
    return get_words(abs(n)).strip()
    
# 8. Calculate the sum of first n even numbers recursively. 
def sum_even(n:int):
    n = abs(n)
    if n == 0:
        return 0
    if n == 1:
        return 2
    return 2*n + sum_even(n-1)

# 9. Calculate the sum of first n odd numbers recursively.
def sum_odd(n:int):
    n = abs(n)
    if n == 0:
        return 0
    return (2*n)-1 + sum_odd(n-1) 
# CodeWithNishchal
# 10. Find nCr (Combination formula) recursively using Pascal’s relation.
def nCr(n: int, r: int):
    if r>n:
        return 0
    if r==0 or r==n:
        return 1 
    return nCr(n-1,r-1) + nCr(n-1,r)
print(nCr(5,2))