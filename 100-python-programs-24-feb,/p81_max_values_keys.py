n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

max_key = max(d, key=d.get)
print(max_key)

// input  : 
3
a 10
b 25
c 15
// output :  
 b