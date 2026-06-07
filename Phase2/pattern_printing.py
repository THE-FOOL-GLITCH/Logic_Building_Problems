# 1. Print n Stars on the Same Line
def print_stars(n:int):
    for i in range(n):
        print("*",end="")
    print()    

# 2. Print Square of Stars (nXn)

def print_square_stars(n:int):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
            
# 3. Print an Increasing Triangle of Stars

def print_increasing_triangle(n:int,a:str):
    for i in range(1,n+1):
        for j in range(i):
            print(a,end="")
        print()

# 4. Print a Right-Aligned Triangle of Stars  

def print_right_triangle(n:int,a:str)->None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i+1):
                print(a,end="")    
        print()

# 5. Print Stars in Even Numbers (2, 4, 6, 8, 10)

def print_even_stars(n:int)->None:
    for i in range(1,n+1):
        for j in range(i*2):
            print("*",end="")
        print()    

# 6: Print Stars in Odd Numbers (1, 3, 5, 7, 9)

def print_odd_stars(n:int)->None:
    for i in range(n+1):
        for j in range((2*i) + 1):
            print("*",end="")
        print()  
# 7: Print a Centered Pyramid of Stars  

def print_centered_pyramid(n:int)->None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()    

# 8: Print Stars and Spaces Alternating

def print_alternating_pyramid(n:int)->None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            if k%2 == 0:
                print("*",end="")
            else:
                print(" ",end="") 
        print()    

# 9. Print Numbers in an Increasing Sequence

def print_increasing_numbers(n:int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()    

# 10: Print Repeated Numbers per Row

def print_repeated_numbers(n:int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

# 11. Floyd's Triangle (Continuous Number Ramping)

def print_floyds_triangle(n:int):
    num = 1
    for i in range(n+1):
        for j in range(i):
            print(num,end=" ")
            num += 1
        print()    

# 12. print_wrapped_floyds_triangle

def print_wrapped_floyds_triangle(n:int):
    num = 1
    for i in range(n+1):
        for j in range(i):
            print(num,end=" ")
            if num == 0:
                num+=1
            elif 1<=num<9:
                num += 1
            else:
                num = 0
        print()    

# 13: The Alternating Binary Matrix

def print_binary_triangle(n:int):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if (i+j)%2 == 0:
                print(1,end="")
            else:
                print(0,end="")    
        print()

# 14: Alphabetical Floyd's Triangle

def print_alphabet_floyd(n:int):
    start = ord("A")
    for i in range(1,n+1):
        for j in range(i):
            print(chr(start),end="")
            start += 1
        print()    


# 15: Constant Character Rows

def print_constant_char_rows(n:int):
    start = ord("A")
    for i in range(1,n+1):
        for j in range(i):
            print(chr(start),end=" ")
        start += 1
        print()    

# 16: Increasing Character Sequence Per Row

def print_increasing_char_sequence(n:int):
    start = ord("A")
    for i in range(1,n+1):
        for j in range(i):
            print(chr(start),end=" ")
            start += 1
        print()
        start = ord("A")    

# 17: The Alphabet Pyramid (Continuous String)

def print_alphabet_pyramid(n:int):
    start = ord("A")
    for i in range(0,n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(((2*i)+1)):
            print(start,end="") 
            start += 1       
        print()

# 18: The Palindromic Number Pyramid

def print_palindromic_pyramid(n:int):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(1,i+2):
            print(k,end="")
        for l in range(i,0,-1):
            print(l,end="")        
        print()    

# 19: The Diamond Star Matrix (Symmetric Merging)

def print_diamond(n:int):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i + 1):
            print("*",end="")
        print() 
    for i in range(n-2,-1,-1):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i + 1):
            print("*",end="")
        print()        
       

# 20: The Inverted Palindromic Number Pyramid

def print_inverted_palindromic_pyramid(n:int):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i+1):
            print(n-k,end="")  
        for l in range(n-i+1,n+1):
            print(l,end="")   
        print()      
