temp = 65
for i in range(1, 9, 1):
    for j in range(1, i + 1, 1):
        print("%c" %temp, end = "")
    temp += 1
    print()