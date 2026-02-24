# Read number from standard input
num = int(input())

# Check even or odd without using modulus
# Method: If integer division by 2 multiplied back equals original number, it's even
if (num // 2) * 2 == num:
    print("Even")
else:
    print("Odd")

// input:
    10
//output: 
   even 