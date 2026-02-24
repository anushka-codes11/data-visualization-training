lst = list(map(int, input().split()))
lst = [x if x >= 0 else 0 for x in lst]
print(*lst) 
// input: 
1 -2 3 -4 5
// output : 
1 0  3 0 5