import time
import sys
import json
import matplotlib.pyplot as plt
import math

sys.setrecursionlimit(10**6)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

file=open("ex2.json")
ex2=json.load(file)


funcTime=[]
for i in ex2:
    start= time.time()
    func1(i, 0, len(i)-1)
    print("f")
    end=time.time()
    funcTime.append(end-start)

print("OUT")

plt.scatter([0,1,2,3,4], funcTime)
plt.legend()
plt.xlabel("Array #")
plt.ylabel("Time (s)")
plt.show()