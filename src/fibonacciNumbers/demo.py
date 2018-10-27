# 斐波那契数列
def fib(num):
    a = 0
    b = 1
    n = 0
    yield a
    while n < num:
        a, b = b , a + b
        yield a
        n += 1
    print('done')

for i in fib(9):
    print(i)
fib(9)