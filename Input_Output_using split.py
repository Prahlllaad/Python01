#1
# Taking input from the user
name = input("Enter your name: ") #Input Command

print("Hello, " + name) #Output Command
print(type(name))
Enter your name: PRAHLAD GURJAR
Hello, PRAHLAD GURJAR
<class 'str'>
#2
# Taking input from the user as integer
num = int(input("Enter a number: "))
 
add = num + 1
 
# Output
print(add)
Enter a number: 16
17
#3
# Output Command
# print() method
print("HII")
HII
#4
# print() method
print("HII", end = "!")
 
# code for disabling the softspace feature 
print('H', 'H', 'I', sep="#")
HII!H#H#I
#5
#Formatting
name = "PRAHLAD"
print(f'Hello {name}! How are you?')
Hello SPRAHLAD! How are you?
#6
#Addition and subtraction Program with formated output
a = 22
b = 13
 
# addition
sum = a + b
 
# subtraction
sub = a- b
 
# Output
print('The value of a is {} and b is {}'.format(a,b))
 
print('{2} is the sum of {0} and {1}'.format(a,b,sum))
 
print('{sub_value} is the subtraction of {value_a} and {value_b}'.format(value_a = a ,
                                                                         value_b = b,
                                                                         sub_value = sub))
The value of a is 22 and b is 13
35 is the sum of 22 and 13
9 is the subtraction of 22 and 13
#7
#Python String split()
text = 'Python is a fun programming language'

# split the text from space
print(text.split(' '))
['Python', 'is', 'a', 'fun', 'programming', 'language']
#8
#Split using Separator
langs = 'C,Python,R,Java,SQL,Hadoop'
print(langs.split(','))

fruits = 'apples$banana$mango$fig$pear'
print(fruits.split('$'))
['C', 'Python', 'R', 'Java', 'SQL', 'Hadoop']
['apples', 'banana', 'mango', 'fig', 'pear']
#9
# multiple input using split
 
# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()
 
# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of teachers: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()
Enter a two value: 4 6
Number of boys:  4
Number of girls:  6

Enter a three value: 9 2 7
Total number of teachers:  9
Number of boys is :  2
Number of girls is :  7
