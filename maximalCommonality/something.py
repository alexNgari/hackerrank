
def number_sort(jumbledList, mapList):
    mapDict = {}
    outDict = {}
    output = []
    for i, x in enumerate(mapList):
        mapDict[str(x)] = i
    print(mapDict)
    for i in jumbledList :
        right_one=""
        for b in i:
            right_one=right_one+str(int(mapDict[b]))
        outDict[right_one] = i
    print(outDict)
    sortedDict = sorted(outDict)
    output = [outDict[key] for key in sortedDict]

    print(output)

s1=['12','02','4','023','65','83','224','50']
number_sort(s1,[2,1,4,8,6,3,0,9,7,5])
