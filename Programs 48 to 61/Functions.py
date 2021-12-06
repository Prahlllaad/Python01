#48)Write a Python function that takes a list of words and returns the length of the longest one.
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["CS", "ACROPOLIS", "CSIT"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
Longest word:  ACROPOLIS
Length of the longest word:  9

#49.Write a function x(n) for computing an element in the sequence xn=n^2+1. Call the function for n=4 and write out the result.

def x(n):
  return(n**2 + 1)

print(x(4))
17

#50. Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string slicing to extract the portion 
#of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

string = 'Y-tatata-acropolis: 0.8475'
col_pos = string.find(':')                  # Finds the colon character
number = string[col_pos + 1:]                 # Extracts portion after colon
confidence = float(number)                  # Converts to floating point number
print(confidence)
0.8475

#51. Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.

def middleOfThree(a, b, c) :
	if a > b :
		if (b > c):
			return b
		elif (a > c) :
			return c
		else :
			return a
	else:
		if (a > c) :
			return a
		elif (b > c) :
			return c
		else :
			return b

a = 20
b = 45
c = 40
print( middleOfThree(a, b, c) )
40

#52.Write a function that computes the area of a rectangle. Then, write a second function that calls this function three times to compute the surface area of a rectangular solid.
def secondfun():
  for i in range(3):
    print(area(i+1,i+3))

def area(h,w):
  area=h*w
  return area
height=2
width=3
print(area(height,width))

secondfun()
6
3
8
15

#53.Create an outer function that will accept three parameters, a, b and c. Create an inner function inside an outer function that will calculate the
#addition of a, b and c. At last, an outer function will add 5 into addition and return it 
def num1(x,y,z):
  def num2(a,b,c):
    return a+b+c
  outer=num2(x,y,z)+5
  return outer

print(num1(5,4,5))
19

#54.Write a program to create a recursive function to calculate the product of numbers from 10 to 100.

def recur(n):
   if n == 10:
       return n
   else:
       return n*recur(n-1)

print("the product of numbers from 10 to 100 : " "is", recur(100))
the product of numbers from 10 to 100 : is 257182031095525112107857249934597388918419224714455526533820998388496472644482792132224051962512451185663850090463028434334174412800000000000000000000000

#55.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number : "))
print(factorial(n))
Input a number : 5
120

#56.Write a Python function to display all the multiples of  7 & 9 within the range 100 to 500.
nl=[]
for x in range(100, 501):
    if (x%7==0) and (x%9==0):
        nl.append(str(x))
print (','.join(nl))
126,189,252,315,378,441

#57.Write a Python function  to check whether the given integer is a prime number or not.
num = 27
flag = False
def prime(n):
  flag1=False
  if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag1 = True
            break
  return flag1

flag=prime(num)
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
27 is not a prime number

#58. Write a Python function that checks whether a passed interger is armstrong or not.

n = int(input("Enter a number: "))

def armstrong(num):
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  return sum

summ=armstrong(n)
if n == summ:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
Enter a number: 407
407 is an Armstrong number

#59. Program to return a function from another function.

def B():
	print("Inside the method B.")
	
def A():
	print("Inside the method A.")
	return B

returned_function = A()

returned_function()
Inside the method A.
Inside the method B.

#60. First, def a function, start_process, that takes one argument p. Then, if the start_process function receives an p equal to "Yes",
# it should return "Start Process" Alternatively, elif p is equal to "No", then the function should return "Start Process Aborted".
#  Finally, if start_process gets anything other than those inputs, the function should return "Sorry for the input".

def start_process(p):
  if p=="Yes":
    return "Start Process"
  elif p=="No":
    return "Start Process Aborted"
  else:
    return "Sorry for the input"

command= input("Enter a command: ")
print(start_process(command))
Enter a command: Yes
Start Process

#61. First, def a function called calculate_distance, with one argument (choose any argument name you like).
#   If the type of the argument is either int or float, the function should return the absolute value of the function input.
#   Otherwise, the function should return "No value". Check if it works calling the function with  9.6 and "what?".

def calculate_distance(argument):
  if type(argument) == int or type(argument) == float:
      return abs(argument)
  else:
      print("No value")

print("the absolute value : " ,calculate_distance(33.20))

calculate_distance("what?")
the absolute value :  33.2
No value
