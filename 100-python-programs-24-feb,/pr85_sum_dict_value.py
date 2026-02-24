n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

print(sum(d.values()))

// input : 

3
a 10
b 20
c 30
//output: 
  60