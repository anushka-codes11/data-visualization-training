lst = list(map(int, input().split()))
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(*lst) 

// input : 
4 2 5 1 3
// output : 
1,2,3,4,5