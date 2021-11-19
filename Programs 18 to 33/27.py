n = list(map(int, input("Enter a Number:").split()))
n1 = []
for i in n:
    if i not in n1:
        n1.append(i)
if len(n) == len(n1):
    print("Number is a Unique Number. ")
else:
    print("Number is not a Unique Number. ")