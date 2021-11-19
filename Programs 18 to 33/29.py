import math
n = int(input("Enter a Number: "))
flag = 0
for i in range(2, int(math.sqrt(n)) + 1, 1):
    if n % i == 0:
        flag = 1
        break
if n == 1:
    print(n, " is neither prime nor a composite number.")
else:
    if flag == 0:
        print(n, " is a prime number. ")
    else:
        print(n, " is not a prime number. ")