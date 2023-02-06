<<<<<<< HEAD
memo={}
def func(n):
    if n==0 or n==1:
        return n
    else:
        if n not in memo:
            memo[n]= func(n-1)+func(n-2)
        return memo[n]
=======
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
>>>>>>> 4e40c870b851ba7c9c07a6817d9efd999823acab
