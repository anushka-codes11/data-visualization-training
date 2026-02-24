s = input().split()
result = []
for word in s:
    result.append(word[0].upper() + word[1:].lower())
print(" ".join(result))

//input
hello world
//output
Hello World