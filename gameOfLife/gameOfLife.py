
import numpy as np
import scipy.signal as sc

def parseState(dotCrossArray):
    dotCrossArray = np.array(dotCrossArray)
    return np.where(dotCrossArray=='.', 0, 1)
# print(parseState([['.', 'X', '.'],['.','X','.'],['.','X','.']]))

def unparseState(parsedState):
    return np.where(parsedState==0, '.', 'X').tolist()
# print(unparseState(np.array([[0,1,0],[0,1,0],[0,1,0]])))

def countLiveNeighbours(parsedState):
    filter = np.array([[1,1,1],[1,0,1],[1,1,1]])
    return sc.convolve2d(parsedState, filter, mode='same', boundary='fill', fillvalue=0)
# countLiveNeighbours(np.array([[0,1,0],[0,1,0],[0,1,0]]))


def applyRules(parsedState, neighboursCounts):
    ruleGrid = np.array([0,0,1,1,0,0,0,0,0])
    toRetain = np.where(neighboursCounts==2)
    valuesToRetain = parsedState[toRetain]
    evolvedState = ruleGrid[neighboursCounts]
    evolvedState[toRetain] = valuesToRetain
    return evolvedState
# print(applyRules(np.array([[0,1,0],[0,1,0],[0,1,0]]), countLiveNeighbours(np.array([[0,1,0],[0,1,0],[0,1,0]]))))

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