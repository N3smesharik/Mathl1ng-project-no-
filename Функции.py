def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
def minch(A):
    mn = 1000000000000
    for i in range(1, len(A), 2):
        if mn > A[i]:
            mn = A[i]
    return mn
def check(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
def bank(a, y):
    for i in range(y):
        a += a / 10
    return a
def check1(a):
    i = 2
    while i < n ** 0.5:
        if a % i == 0:
            return False
        i += 1
    return True
def nodinok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b), a + b
n = int(input())
A = list(map(int, input().split()))
s = input()
a, y = map(int, input().split())
b, c = map(int, input().split())
print(fib(n))
print(minch(A))
print(check(s))
print(bank(a, y))
print(check1(n))
print(nodinok(b, c))
