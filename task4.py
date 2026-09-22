if __name__ == '__main__':
    n = int(input("Input a number: "))

    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    print("The factorial of", n, "is:", factorial)