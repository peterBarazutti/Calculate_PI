import random
import time

def calcProcess():
    numOfIterations = 1000000;
    pointsInsideCircle = 0;
    for i in range(numOfIterations):
        xCoord = random.random()
        yCoord = random.random()
        distance = pow(xCoord,2) + pow(yCoord, 2)
        if not distance > 1:
            pointsInsideCircle += 1
    valueOfPI = (pointsInsideCircle/numOfIterations)*4
    return valueOfPI

start = time.time()
print(calcProcess())
end = time.time()
print(end - start)