import time
import matplotlib.pyplot as plt

memo={}
def func(n):
    if n==0 or n==1:
        return n
    else:
        if n not in memo:
            memo[n]= func(n-1)+func(n-2)
        return memo[n]

def func1(n):
    if n==0 or n==1:
        return n
    else:
        return func1(n-1)+func1(n-2)

funcTime=[]
func1Time=[]
numi=[]
for i in range(36):
    start= time.time()
    func(i)
    end=time.time()
    funcTime.append(end-start)

    start1= time.time()
    func1(i)
    end1=time.time()
    func1Time.append(end1-start1)
    numi.append(i)

figure=plt.figure()
funcT=figure.add_subplot(111)
funcT.scatter(numi, funcTime, c="b", label="With memoization", alpha=0.5)
funcT.scatter(numi, func1Time, c="r" ,label="Without memoization", alpha=0.5)
plt.legend()
plt.xlabel("ith fibinochi number")
plt.ylabel("Time (s)")
plt.show()
