lst = list(map(int, input().split()))
k = int(input())
k %= len(lst)
rotated = lst[-k:] + lst[:-k]
print(*rotated)

// input : 
  1 2 3 4 5
// output: 
   4 5 1 2 3