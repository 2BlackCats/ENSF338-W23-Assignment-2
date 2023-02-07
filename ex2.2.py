import time
import sys
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
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
    end=time.time()
    funcTime.append(end-start)
label=[i for i in range(len(ex2))]

plt.scatter(label, funcTime, c="b", label="Sorting algorithom", alpha=0.5)
plt.legend()
plt.xlabel("Array #")
plt.ylabel("Time (s)")
plt.show()