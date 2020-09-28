#%%
a = list('bac')
b = list(a[::-1])
palindrome = []

for x in a:
    if x in b:
        palindrome.append(x)
        b = b[b.index(x)+1:]

''.join(palindrome)




# %%
