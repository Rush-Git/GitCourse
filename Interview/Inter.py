#In a given string how many times each letter is repeated.

s = "INTERVIEW"
count = 0
target = 'R'

for i in s:  #-- for I in INTERVIEW
    if i == target:  #---- if I == I
        count += 1  #----- Count = Count + 1; 0 = 0+1 = 1
print(count)

W = "INTERVIEW"
CountI = s.count('I')
print("Count of I is", CountI)
CountN = s.count('N')
print("Count of N is", CountN)
CountT = s.count('T')
print("Count of T is", CountT)
CountE = s.count('E')
print("Count of E is", CountE)
CountR = s.count('R')
print("Count of R is", CountR)
CountV = s.count('V')
print("Count of V is", CountV)
CountW = s.count('W')
print("Count of W is", CountW)

# Program to check if a number is prime or not


