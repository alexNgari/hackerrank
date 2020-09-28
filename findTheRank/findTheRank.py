import numpy as np
def findTheRank(rank, data):
    data = np.array(data)
    sums = np.sum(data, axis=1)
    ranks = np.argsort(-1*sums, kind='mergesort')
    return ranks[rank-1]

testArr = [[80,96,81,77],[78,71,93,75],[71,98,70,95],[80,96,89,77]]
print(findTheRank(3, testArr))