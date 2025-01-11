#Palindrome

p = "malayalam"[::-1]

#y = reversed(p)
print(p)

#code to return non duplicate values from array

l = (1, 2, 3, 2, 1, 4, 5, 3, 2, 5, 7)

m = set(l)
print(m)

#prime numbers

numb = 34

if numb == 0 and numb == 1:
    print("the number is not a prime number")
elif numb > 1:
    for i in range(2, numb):
        if (numb % i) == 0:
            print("the number is not a prime number")
        else:
            print("the number is a prime number")
        break

#How will you separate the numbers from the string

strng = "I 143 python"
print(strng)

numbe = [int(words) for words in strng.split() if words.isdigit()]
print(numbe)

#in a given string how many times each letter is repeated

s = "INTERVIEW"
count = 0
targets = "E"
#r = s.count("I")
for i in s:
    if i == targets:
        count += 1
print(count)

# febonacci series:

n = 10
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
    print()


#return only vowels
def vowelorconsonent(x):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        print("Vowel")
    else:
        print("Consonent")


vowelorconsonent('r')

from collections import Counter

st = "INTERou in life"
v = 'aeiouAEIOU'
count = Counter([i for i in st if i in v])
print(count)


#check even or odd

if n in range(2,5) and (n % 2 == 0):
        print('Not Weird')
    elif n in range(6,20) and (n % 2 == 0):
        print('Weird')
    elif n > 20 and (n % 2 == 0):
        print('Not Weird')
    else:
        print('Weird')

#The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

for i in range(n):
        print(i*i)


#leap year:
if (year % 4 == 0 and year % 100 != 0)or year % 400 ==0:
        return True
    else:
        return False

#for given n=5 print output as 12345:
for i in range(n):
        print(i+1, end ="")

#reduce:
t = Fraction(reduce(lambda x, y: x* y, fracs))


