def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

a, b = map(int, input().split())
print(power(a, b))

// input :  
2,5
// output : 
    32