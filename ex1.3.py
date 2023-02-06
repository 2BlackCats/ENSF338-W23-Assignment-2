memo={}
def func(n):
    if n==0 or n==1:
        return n
    else:
        if n not in memo:
            memo[n]= func(n-1)+func(n-2)
        return memo[n]