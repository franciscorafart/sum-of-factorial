def factorial(x):
    total = 1
    for y in range(1,x):
        total *= y
    return total

def sumOfFactorial(x):
    xStr = str(x)
    total = 0

    arr = list(xStr)

    for ch in arr:
        s_temp = int(ch)
        total += s_temp

    return total


print sumOfFactorial(factorial(100))
