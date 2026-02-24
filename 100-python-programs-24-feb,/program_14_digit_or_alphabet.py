# Read a single character from standard input
char = input().strip()

# Check if input is a single character
if len(char) == 1:
    if char.isdigit():
        print("Digit")
    elif char.isalpha():
        print("Alphabet")
    else:
        print("Special Character")
else:
    print("Invalid Input") 

// input : 
    5
// Output:  
   digit 
