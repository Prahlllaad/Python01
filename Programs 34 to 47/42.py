#Write a Python program to count occurrences of a substring in a string.
s = input("Enter a String: ")
n = int(input("Enter Number of Characters to LowerCase: "))
print(s[:n].lower() + s[n:])