#%%
import numpy as np

#%%
def mapForward(mapping, arr):
    arr_n = []
    for num in arr:
        dig = ''.join([str(mapping.index(int(d))) for d in num])
        print('dig', dig)
        arr_n.append(int(dig))

    return arr_n

#%%
def sortStuff(arr_n):
    
    
# %%
