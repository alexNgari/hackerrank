import re

def decToBin(decimalNum):
    return bin(decimalNum)[2:]

def longestConsecutiveOnes(decNum):
    binaryNum = decToBin(decNum)
    pattern = re.compile(r'1+')
    matches = pattern.findall(binaryNum)
    return max(list(map(len, matches)))
     
print(longestConsecutiveOnes(13))