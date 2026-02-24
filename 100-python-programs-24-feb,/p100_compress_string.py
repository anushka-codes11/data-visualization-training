# File Name: compress_string.py

# Read input from standard input
input_string = input().strip()

# Check if input is empty
if not input_string:
    print("")
else:
    compressed = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed += input_string[i - 1] + str(count)
            count = 1

    # Add last character and its count
    compressed += input_string[-1] + str(count)

    print(compressed)

    // input : 
      aaabbc
    // output: 
      a3b2c1