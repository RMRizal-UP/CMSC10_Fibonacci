def fibonacci(n):
    f_one = 1
    f_two = 0
    for i in range(n - 1):
        fib_num = f_one + f_two
        f_one = f_two
        f_two = fib_num
        print(fib_num)
    return fib_num


#main function
n = int(input("Enter number for the Fibonacci sequence: "))
fibonacci(n)