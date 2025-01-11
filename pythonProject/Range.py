def fizz_buzz():
    for i in range(1, 51):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)


fizz_buzz()


def factorial_of_a_num(num):
    fact = 1
    for i in range(number, 1, -1):
        fact *= i
    return fact


number = int(input("Enter the number:"))
print(factorial_of_a_num(number))

