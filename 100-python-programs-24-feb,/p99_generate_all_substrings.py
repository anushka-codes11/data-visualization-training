# File Name: generate_all_substrings.py

# Read input from standard input
input_string = input().strip()

# Check if input is empty
if not input_string:
    print("No substrings")
else:
    n = len(input_string)
    
    # Generate all substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(input_string[i:j])

            // input : 
            abc
            // output:
            a
            ab
            abc
            b
            bc
            c