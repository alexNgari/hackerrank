#%%
import numpy as np
#%%
def play(arr):
    Tom = []
    Jerry = []
    arr = np.array(arr)
    for i in range(arr.shape[1]):
        flattenedMaxIndex = np.argmax(arr)    
        if i%2==0:
            Tom.append(arr.flatten()[flattenedMaxIndex])
        else:
            Jerry.append(arr.flatten()[flattenedMaxIndex])
        maxColumn = int(flattenedMaxIndex%arr.shape[1]) 
        arr = np.delete(arr, maxColumn, axis=1)
        # print(arr)
    # print(Tom)
    # print(Jerry)
    return sum(Tom)-sum(Jerry)

arr = [[5, 7, 6, 2, 8, 4, 4, 8],
[2, 5, 4, 5, 9, 8, 4, 2],
[5, 4, 3, 9, 8, 3, 3, 4],
[4, 9, 3, 4, 6, 7, 4, 9],
[2, 4, 6, 2, 9, 2, 4, 2]]
play(arr)

# %%
