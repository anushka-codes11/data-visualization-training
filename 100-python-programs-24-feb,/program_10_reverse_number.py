# Read number from standard input
num = int(input())

# Store the sign of number
sign = -1 if num < 0 else 1

# Work with positive number
n = abs(num)
rev = 0

# Loop to reverse the number
while n > 0:
    digit = n % 10       # Get last digit
    rev = rev * 10 + digit
    n = n // 10          # Remove last digit

# Apply original sign
rev = rev * sign

# Print the reversed number
print(rev)

// input:
   1234
//output: 
   4321   