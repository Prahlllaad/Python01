s = input("Enter a String: ")
s1 = ''
for i in range(len(s)):
    if i == ' ':
        s1.insert(i)
s = s.replace(' ', '')
s1 += s
s = s1
print("New String: ", s)