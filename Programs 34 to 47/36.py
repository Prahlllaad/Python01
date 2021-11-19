s = input("Enter a String: ")
if len(s) >= 3:
    if s.endswith('polis'):
        s += 'CS'
    else:
        s += 'polisCS'
print(s)