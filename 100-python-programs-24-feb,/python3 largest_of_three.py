# Read three numbers from standard input
a = int(input())
b = int(input())
c = int(input())

# Check the largest number
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c) 


// input :  
    10
    25
    15 
// output: 
    25