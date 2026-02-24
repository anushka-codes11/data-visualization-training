keys = input().split()
values = list(map(int, input().split()))

d = dict(zip(keys, values))
for k in d:
    print(k, d[k]) 

    // input : 
    a b c
    1 2 3 
    // output :  
     a 1  
    b 2
    c 3