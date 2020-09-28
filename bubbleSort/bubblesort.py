#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swaps = 0
while True:
    num_swaps = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            num_swaps+=1
            swaps+=1
        
    if num_swaps == 0:
        break

print(f'Array is sorted in {swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')