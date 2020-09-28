#%%
import numpy as np
import scipy.signal as sc
#%%
def gridGame(array, noOfTurns, ruleGrid):
    array = np.array(array)
    ruleGrid = [int(x=='alive') for x in rules]
    print(ruleGrid)
    ruleGrid = np.array(ruleGrid)
    filter = np.array([[1,1,1],[1,0,1],[1,1,1]])
    for _ in range(noOfTurns):
        mask=sc.convolve2d(array, filter, mode='same', boundary='fill', fillvalue=0)
        array = ruleGrid[mask]
        # print(array)
    return array.tolist()

array = [[0,1,0,0],[0,0,0,0]]
rules = ['dead','alive','dead','dead','dead','alive','dead','dead','dead']
print(gridGame(array, 2, rules))

# %%
