### 斐波那锲数列 Fibonacci Numbers Demo

**Problem Description 问题描述**

The Fibonacci sequence is the sequence of numbers such that every element is equal to the sum of the two previous elements, except for the first two elements f0 and f1 which are respectively zero and one.

斐波那锲数列是一串数字：第一个数字是0，第二个数字是1，之后的每个数字都是前两个数字的和。

e.g：

```
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

// output
0
1
1
2
3
5
8
13
21
34
```