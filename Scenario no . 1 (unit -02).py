# Fibonacci using Memoization

def fibonacci(n, memo):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


# Accept an integer N
N = int(input("Enter the value of N: "))

# Memoization dictionary
memo = {}

# Generate and display first N Fibonacci numbers
print("Fibonacci Sequence:")

for i in range(N):
    print(fibonacci(i, memo), end=" ")
