#!/usr/bin/python

# BadNeighbors Dynamic Programming Problem from TopCoder
# http://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009

donations = [10, 3, 2, 5, 7, 8 ] # returns 19: [10 + 2 + 7]
donations_two = [11, 15] # returns 15
donations_three = [7, 7, 7, 7, 7, 7, 7] # returns 21
donations_four = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # returns 16
donations_five = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
                  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
                  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72] # returns 2926
donations_six = [397, 510, 335, 521, 973, 576, 420, 180, 89, 910, 554, 
                 570, 702, 654, 290, 685, 6, 786, 302, 91, 249, 851, 
                 799, 9, 879, 387, 292, 628, 129, 714, 449, 78, 717, 
                 159, 650, 281, 869, 271, 253, 364] # returns 11488

def maximizeDonations(donations):
    solution = []
    zeroUsed = []
    maxDonation = 0;
    
    # Base cases
    if(len(donations) == 1):
        return donations[0]
    elif(len(donations) == 2):
        return max(donations[0], donations[1])
    
    solution.append(donations[0])
    zeroUsed.append(1)
    solution.append(donations[1])
    zeroUsed.append(0)
    
    for i in range(2, len(donations)):
        solution.append(0);
        zeroUsed.append(0);
        for j in range(len(solution) - 2):
            if solution[j] + donations[i] >= solution[i]:
                # Mark when the zero index was used
                if zeroUsed[j] == 1:
                    zeroUsed[i] = 1
                else:
                    zeroUsed[i] = 0
                if i == len(donations) - 1 and zeroUsed[j] == 1:
                    solution[i] = solution[j] + donations[i] - donations[0]
                    zeroUsed[i] = 0
                else:
                    solution[i] = solution[j] + donations[i]
                maxDonation = max(maxDonation, solution[i])
    return maxDonation

print maximizeDonations(donations)
print maximizeDonations(donations_two)
print maximizeDonations(donations_three)
print maximizeDonations(donations_four)
print maximizeDonations(donations_five)
print maximizeDonations(donations_six)