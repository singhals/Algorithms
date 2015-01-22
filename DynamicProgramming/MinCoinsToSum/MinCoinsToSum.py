#!/usr/bin/python

coinList = [1, 3, 5, 10, 2]
sumSize = 12
sumList = []

for i in range(0, sumSize):
    sumList.append(100000000)
sumList[0] = 0;

for i in range(1, sumSize):
    for j in range(len(coinList)):
        coin = coinList[j]
        if coin <= i and (sumList[i - coin]+1) < sumList[i]:
            sumList[i] = sumList[i - coin] + 1
        
print sumList[sumSize-1]