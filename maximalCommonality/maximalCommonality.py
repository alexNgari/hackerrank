#%%
def findCommonality(inputStr):
    inputStr = list(inputStr)
    commonalities = []
    for i in range(len(inputStr)-2):
        commonChars = set(inputStr[:i+1]).intersection(set(inputStr[i+1:]))
        commonality = 0
        for x in commonChars:
            commonality += min([inputStr[:i+1].count(x)]+[inputStr[i+1:].count(x)])
        # commonalities.append(sum[(min([inputStr[:i+1].count(x)].append(inputStr[i+1:].count(x)))) for x in commonChars])
        commonalities.append(commonality)
    return max(commonalities)

print(findCommonality('aabbbbaa'))
#%%
inputStr = list('aabbbbaa')
commonalities = []
inputStr

# %%
commonChars = set(inputStr[:5]).intersection(set(inputStr[5:]))
commonChars

# %%
min([inputStr[:5].count('a')]+[inputStr[5:].count('a')])

# %%
