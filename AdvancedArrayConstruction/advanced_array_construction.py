#!/bin/python3

import os
import sys

#
# Complete the arrayConstruction function below.
#
def arrayConstruction(n, s, k):
    #
    arrayOfArrays = []
    if s>k:
        tempArray = [1 for i in range(k)]
        tempArray[-1] = s - (k-1)
        arrayOfArrays.append(tempArray)
        for i in range(k-1):
            while 
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nsk = input().split()

        n = int(nsk[0])

        s = int(nsk[1])

        k = int(nsk[2])

        result = arrayConstruction(n, s, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
