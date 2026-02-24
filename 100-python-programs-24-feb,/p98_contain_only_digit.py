# File Name: check_only_digits.py

# Read input from standard input
input_string = input().strip()

# Check if string contains only digits and is not empty
if input_string and input_string.isdigit():
    print(True)
else:
    print(False)

    //  input:
   123456
   // output :
     True   
