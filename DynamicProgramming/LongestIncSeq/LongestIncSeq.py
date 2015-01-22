#!/usr/bin/python

sequence = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
solution = []
maxLength = 0
    

for i in range(0, len(sequence)):
    solution.append(1);
    for j in range(0, len(solution)-1):
        nextSolution = solution[j]
        if sequence[j] <= sequence[i] and nextSolution+1>solution[i]:
            solution[i] = nextSolution + 1
            maxLength = max(maxLength, solution[i])
            
print solution
print maxLength