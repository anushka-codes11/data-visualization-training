lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
common = list(set(lst1) & set(lst2))
print(*common) 


//  input:  
  1 2 3 4
  3 4 5 6
// output : 
 3 4