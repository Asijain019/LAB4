N = int(input("Enter the term till which you want to print the Fibonacci series: "))
fib_series = [1, 1]  # Start with the first two terms
i = 2  # Index for the next term

while i < N:
    fib_series.append(fib_series[-1] + fib_series[-2])
    i += 1

print("The Fibonacci series till", N, "terms is:\n", fib_series)



