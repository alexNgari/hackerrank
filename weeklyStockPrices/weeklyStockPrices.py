def rollingAve(listX):
    a = ['%.2f'%((i>=6)*sum(listX[i-6:i+1])/7) for i, x in enumerate(listX)][6:]
    print(a)

rollingAve([2,2,2,2,2,2,2,14,14,14,14,14,14,14])