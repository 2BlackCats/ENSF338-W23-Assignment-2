def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

remember = {}
def memoFunc(n):
    if n == 0 or n == 1:
        return n
    if n not in remember:
        remember[n] = n + memoFunc(n-1)
    return remember[n]

print(func(10))
print(memoFunc(10))