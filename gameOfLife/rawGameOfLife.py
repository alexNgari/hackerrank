import sys
def parseState(unParsedState):
    return [[0 if j=='.' else 1 for j in i] for i in unParsedState]
# print(parseState([['.', 'X', '.'],['.','X','.'],['.','X','.']]))

def unparseState(parsedState):
    return [['.' if j==0 else 'X' for j in i] for i in parsedState]
# print(unparseState([[0,1,0],[0,1,0],[0,1,0]]))

def countLiveNeighbours(parsedState):
    liveNeighbours = []
    length = len(parsedState)
    for i in range(length):
        liveNeighbours.append([])
        for j in range(length):
            sum=0
            for x in range(i-1,i+2):
                if x<0 or x>=length:
                    continue
                else:
                    for y in range(j-1,j+2):
                        if y<0 or y>=length or (x==i and y==j):
                            continue
                        else:
                            sum += parsedState[x][y]
            liveNeighbours[i].append(sum)
    return liveNeighbours
# print(countLiveNeighbours([[0,1,0],[0,1,0],[0,1,0]]))

def applyRules(parsedState, liveNeighbours):
    rules = [0,0,1,1,0,0,0,0,0]
    newGen = []
    for i,x in enumerate(liveNeighbours):
        newGen.append([])
        for j,y in enumerate(x):
            if y==2:
                newGen[i].append(parsedState[i][j])
            else:
                newGen[i].append(rules[y])
    return newGen
# print(applyRules([[0,1,0],[0,1,0],[0,1,0]], countLiveNeighbours([[0,1,0],[0,1,0],[0,1,0]])))

if __name__=='__main__':
    generations = int(input())
    dimensions = int(input())
    unparsedState = [input().split(' ') for _ in range(dimensions)]
    # print(unparsedState)
    parsedState = parseState(unparsedState)
    for _ in range(generations):
        parsedState = applyRules(parsedState, countLiveNeighbours(parsedState))
    unparsedState = unparseState(parsedState)
    for x in unparsedState:
        print(" ".join(x))
