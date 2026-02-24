# Read number from standard input
num = int(input())

# Initialize sum
sum_digits = 0

# Work with positive number
n = abs(num)

# Loop to calculate sum of digits
while n > 0:
    digit = n % 10      # Get last digit
    sum_digits += digit  # Add to sum
    n = n // 10         # Remove last digit

# Print the sum of digits
print(sum_digits) 

//input: 
  1234
//output: 
   10