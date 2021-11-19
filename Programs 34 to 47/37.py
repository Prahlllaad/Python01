s = input("Enter a String: ")
d = {}
for i in s:
    k = d.keys()
    if i in k:
        d[i] += 1
    else:
        d[i] = 1
print(d)