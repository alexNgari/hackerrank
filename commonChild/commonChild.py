# Complete the commonChild function below.
def commonChild(s1, s2):
    s1 = list(s1.upper())
    s2 = list(s2.upper())
    commonChars = []
    for character in s1[:]:
        if not character in s2:
            s1.remove(character)
            while character in s2:
                s2.remove(character)

    
    return len(commonChars)


