def sum_of_digits(n):
    return sum(int(d) for d in str(n))

num = int(input())
print(sum_of_digits(num))

// input: 
   1234
// output:
    10   
   