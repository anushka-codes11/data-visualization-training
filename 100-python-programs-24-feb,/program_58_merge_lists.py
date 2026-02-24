lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
merged = list(dict.fromkeys(lst1 + lst2))
print(*merged)

// input: 
 1 2 3
 2 3 4 
//output:
  1 2 3 4