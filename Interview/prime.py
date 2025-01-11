num = 278
if num == 0 and num == 1:
    print("Its not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
        break


#Largest number in the list:

L =[45, 72, 32]

Lar = max(L)
print(Lar)


#Reverse the string without using the built in method:

l = "BANGALORE"[::-1]

print(l)

#Remove duplicates from the list:

a = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting to a set
a = list(set(a))

print(a)


#How will you separate the numbers from the string

string = "I 143 Python 123"
print(string)

numbers = [int(word) for word in string.split() if word.isdigit()]
print(numbers)


# Python Program to move all zeros to end using two traversals

# Function which pushes all zeros to end
def pushZerosToEnd(arr):
    # Count of non-zero elements
    count = 0

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count

    for i in range(len(arr)):
        if arr[i] != 1:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 1
        count += 1

def bestsolution:
    zeroCount = [x for x in arr if x==0]
    nonZeroCount = [x for x in arr if x!=0]
    return zeroCount + nonZeroCount



def mysolution:
    for i in arr:
        if i == 0:
            zeroCount.append(i)
        else:
            nonZeroCount.append(i)
        return zeroCount + nonZeroCount



if __name__ == "__main__":
    arr = [1, 2, 1, 4, 3, 1, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")

