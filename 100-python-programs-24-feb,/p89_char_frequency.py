s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for k in sorted(freq):
    print(k, freq[k])
    // input: 
    aab
    //output:
    a 2
     b 1