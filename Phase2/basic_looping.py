# 1. Print numbers from 1 to 10. 
i = 1
while i<=10:
    print(i)
    i += 1
# 2. Print all even numbers between 1 and 100. 
def print_even_numbers(limit: int = 100) -> None:
    """Prints all even numbers from 2 up to the limit."""
    for i in range(2, limit + 1, 2):
        print(i, end=" ") # end=" " keeps it from being a giant vertical wall
    print() # New line for the next function

print_even_numbers()
# 3. Print all odd numbers between 1 and 100. 

def print_odd_numbers(limit:int = 100) ->None:
    for i in range(1,limit+1,2):
        print(i, end =" ")
# 4. Print numbers from 10 down to 1. 
def countdown_timer(start:int)->None:
    for i in range(start,0,-1):
        print(i,end=" ")
# 5. Print the table of a given number (n × 1 to n × 10). 
def print_table(n:int)->None:
    for i in range(1,11):
        print(f"{n} X {i:2} = {n*i}")
# 6. Print the sum of first n natural numbers. 
def sum_natural_numbers(n:int) ->int:
    total = 0
    for i in range(1,n+1):
        total += i
    return total    
# 7. Print the sum of all even numbers up to n.

def sum_even_numbers(n:int)->int:
    total = 0
    for i in range(0,n+1,2):
        total += i
    return total    
# 8. Print the sum of all odd numbers up to n. 

def sum_odd_number(n:int)->int:
    total = 0
    for i in range(1,n+1,2):
        total += i
    return total    
# 9. Print the factorial of a given number. 

def factorial(n:int):
    if n<0:
        return("Invalid input n cannot be negative")
    elif n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
# 10. Print the product of digits of a given number.

def get_digit_product(n:int)->None:
    temp = abs(n)
    product = 1
    while temp>0:
        dig = temp%10
        product *= dig
        temp = temp//10
    print(product)

