# Read three sides from standard input
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check triangle validity
if a + b > c and a + c > b and b + c > a:
    # Determine type
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle") 

// input : 
        
    Enter side a: 5
    Enter side b: 5
    Enter side c: 5
//  output :  

     Equilateral Triangle