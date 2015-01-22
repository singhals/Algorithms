#!/usr/bin/python

# ZigZag Dynamic Programming from TopCoder
# http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493

sequence = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8] # zigzag = 1, 17, 5, 13, 10, 16, 8
sequence_two = [1, 7, 4, 9, 2, 5] # zigzag = 1, 7, 4, 9, 2, 5
sequence_three = [44] # zigzag = 44
sequence_four = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sequence_five = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
sequence_six = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
                600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
                67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
                477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
                249, 22, 176, 279, 23, 22, 617, 462, 459, 244]

def longestZigZag(sequence):            
    solution = []
    
    if len(sequence) == 1:
        return 1
    elif len(sequence) == 2:
        return 2
    
    solution.append(1);
    solution.append(2);
    maxLength = 2
    
    for i in range(2, len(sequence)):
        solution.append(1)
        for j in range(i - 1, 0, -1):
                if ((sequence[i] > sequence[j] and sequence[j] < sequence[j-1]) or 
                    (sequence[i] < sequence[j] and sequence[j] > sequence[j-1])) and solution[i] < solution[j]+1:
                    solution[i] = solution[j] + 1
                    maxLength = max(maxLength, solution[i])
            
    print solution
    return maxLength

print longestZigZag(sequence)
print longestZigZag(sequence_two)
print longestZigZag(sequence_three)
print longestZigZag(sequence_four)
print longestZigZag(sequence_five)
print longestZigZag(sequence_six)


                    