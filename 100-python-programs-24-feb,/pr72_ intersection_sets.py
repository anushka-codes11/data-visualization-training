s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
intersection = s1 & s2
print(*sorted(intersection))

//input 
 1 2 3 4
 3 4 5 6 
 // output : 
   3 4