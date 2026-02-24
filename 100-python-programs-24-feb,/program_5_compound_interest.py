# Read inputs from standard input
P = float(input())   # Principal
R = float(input())   # Rate
T = float(input())   # Time

# Calculate Compound Amount
Amount = P * (1 + R/100) ** T

# Calculate Compound Interest
CI = Amount - P

# Print the result
print(CI)


// input:
   1000
    10
    2
// output:    
    210.0