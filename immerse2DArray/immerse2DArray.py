#!/bin/python3

import math
import os
import random
import re
import sys

def hourGlassSummer(arr2D):
    sums = []
    for i in range(len(arr2D)-2):
        for j in range(len(arr2D[0])-1):
            sums.append(sum(arr2D[i][j:j+3])+arr2D[i+1][j+1]+sum(arr2D[i+2][j:j+3]))
    return(max(sums))


arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

print(hourGlassSummer(arr))

# if __name__ == '__main__':
#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
    
#     print(hourGlassSummer(arr))

