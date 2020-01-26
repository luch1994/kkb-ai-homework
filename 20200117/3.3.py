# 返回裴波那契数列的第n项，n从0开始
def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        b, a = a + b, b
        i = i + 1
    return a

print(fib(0))
print(fib(6))

# 0 1 1 2 3 5 8 13 21 34 55
