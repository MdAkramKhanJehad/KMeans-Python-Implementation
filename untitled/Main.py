import math
from PIL import Image

im = Image.open('color.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_values.sort()

k = 0
try:
    k = int(input("Type a number:"))
except ValueError:
    print("This is not a whole number.")

valueList = []
centroid = []
tempCentroid = []
epsilon = 0.0001

for i in range(k):
    valueList.append([])
    centroid.append([])
    tempCentroid.append([])


firstTime = 1


def checkCentroid(first):
    checker = 0

    if first == 1:
        checker = 1
    else:
        for x in range(k):
            tempDistance = math.sqrt(
                (tempCentroid[x][0] - centroid[x][0]) ** 2 + (tempCentroid[x][1] - centroid[x][1]) ** 2 + (
                            tempCentroid[x][2] - centroid[x][2]) ** 2)
            if tempDistance >= epsilon:
                checker = 1

    return checker


totalSize = (len(pixel_values))
counter = 0
for i in range(k):
    for j in range(math.ceil(totalSize / k)):
        valueList[i].append(pixel_values[counter])
        counter += 1
        if counter == totalSize:
            break
    if counter == totalSize:
        break

# for i in range(k):
#     print(valueList[i][0])
#     print("printed")
#
# for s in range((k)):
#     print(len(valueList[s]))

for i in range(k):
    redSum = 0
    greenSum = 0
    blueSum = 0
    for j in range(len(valueList[i])):
        redSum += valueList[i][j][0]
        greenSum += valueList[i][j][1]
        blueSum += valueList[i][j][2]

    if(len(valueList[i])!=0):
        redAvg = redSum / len(valueList[i])
        greenAvg = greenSum / len(valueList[i])
        blueAvg = blueSum / len(valueList[i])

        tempCentroid[i].append(redAvg)
        tempCentroid[i].append(greenAvg)
        tempCentroid[i].append(blueAvg)

# for i in range(k):
#     print(centroid[i][0])
#     print(centroid[i][1])
#     print(centroid[i][2])

count = 0

while checkCentroid(firstTime) == 1:
    firstTime = 0
    print("processing : ", count )
    for i in range(k):
        centroid[i] = tempCentroid[i]

    for i in range(k):
        valueList[i].clear()

    minDistance = 10000
    minDisIndex = 10000

    for i in range(totalSize):
        for j in range(k):
            distance = math.sqrt(
                (pixel_values[i][0] - centroid[j][0]) ** 2 + (pixel_values[i][1] - centroid[j][1]) ** 2 + (
                        pixel_values[i][2] - centroid[j][2]) ** 2)

            if distance < minDistance:
                minDisIndex = j

        valueList[minDisIndex].append(pixel_values[i])

    for i in range(k):
        redSum = 0
        greenSum = 0
        blueSum = 0
        for j in range(len(valueList[i])):
            redSum += valueList[i][j][0]
            greenSum += valueList[i][j][1]
            blueSum += valueList[i][j][2]

        if(len(valueList[i])) :
            redAvg = redSum / len(valueList[i])
            greenAvg = greenSum / len(valueList[i])
            blueAvg = blueSum / len(valueList[i])

            tempCentroid[i].append(redAvg)
            tempCentroid[i].append(greenAvg)
            tempCentroid[i].append(blueAvg)
    count+=1

for i in range(k):
    centroid[i] = tempCentroid[i]

tempMinDis = 10000
tempMinDisIdex = 10000

pix = im.load()
for p in range(width - 1):
    for q in range(height - 1):
        tempMinDis = 10000
        tempMinDisIdex = 10000

        for j in range(k):
            distance = math.sqrt(
                (pix[p, q][0] - centroid[j][0]) ** 2 + (pix[p, q][1] - centroid[j][1]) ** 2 + (
                            pix[p, q][2] - centroid[j][2]) ** 2)
            #print(distance)
            if distance < tempMinDis:
                tempMinDis = distance
                tempMinDisIdex = j
                #print("TEMP: ", tempMinDisIdex)
        #print(math.ceil(centroid[tempMinDisIdex][0]), " " , math.ceil(centroid[tempMinDisIdex][1]), " ", math.ceil(centroid[tempMinDisIdex][2]))
        pix[p, q] = (math.ceil(centroid[tempMinDisIdex][0]), math.ceil(centroid[tempMinDisIdex][1]),
                     math.ceil(centroid[tempMinDisIdex][2]))

im.save("color.png")
print("image saved")
