import math
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

#Function to find minimum arguments of a 2D array
def returnminArgs(arr, pointsID):
	minD = sys.maxsize
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i][j] < minD:
				minD = arr[i][j]
				argX = pointsID[i]
				argY = pointsID[j]
	return argX, argY

#Function to combine a pointsID and minArgs array to form a clustered array
def combine(pointsID,minArgs):
	clusteredPoints = list(pointsID)

	for elements in minArgs:
		clusteredPoints.remove(elements)

	clusteredPoints.append(minArgs)
	return clusteredPoints

def returnSimpleList(compList, simpleList):
	for elements in compList:
		if isinstance(elements,list):
			simpleList.extend(returnSimpleList(elements,simpleList))
		else:
			simpleList.append(elements)
	return simpleList

#input
nosOfPoints = int(input())
matrixOfPoints = list()
pointID = list()
for i in range(nosOfPoints):
	temp = list(map(float,input().split()))
	matrixOfPoints.append(temp)
	pointID.append(i)

#initialization of basic distance between two IDs
distanceBetweenPoints = [ [0]*nosOfPoints for i in range(nosOfPoints) ]

for i in range(nosOfPoints):
	for j in range(nosOfPoints):
		dist = math.sqrt((matrixOfPoints[i][0]-matrixOfPoints[j][0])**2+(matrixOfPoints[i][1]-matrixOfPoints[j][1])**2)
		if i == j:
			dist = sys.maxsize
		distanceBetweenPoints[i][j] = dist

for x in distanceBetweenPoints:
	print(*x)

minArgs = list(returnminArgs(distanceBetweenPoints,pointID))
clusteredPoints = combine(pointID, minArgs)
print(*clusteredPoints)

while len(clusteredPoints) != 1:
	#Initialization of distance matrix
	distMatrix = [ [0]*len(clusteredPoints) for i in range(len(clusteredPoints)) ]
	print("distance matrix", distMatrix,clusteredPoints)
	for i in range(len(clusteredPoints)):
		distMatrix[i][i] = sys.maxsize


	for i in range(len(clusteredPoints)):
		for j in range(len(clusteredPoints)):
			if i == j:
				continue
			yAxis = [clusteredPoints[j]]
			xAxis = [clusteredPoints[i]]
			distMin = sys.maxsize
			if isinstance(clusteredPoints[i],list):
				xAxis = returnSimpleList(clusteredPoints[i],list())
			if isinstance(clusteredPoints[j],list):
				yAxis = returnSimpleList(clusteredPoints[j],list())
			for elementsX in xAxis:
				for elementsY in yAxis:
					if distMin > distanceBetweenPoints[elementsX][elementsY]:
						distMin = distanceBetweenPoints[elementsX][elementsY]
			distMatrix[i][j] = distMin

	# for x in distMatrix:
	# 	print(*x)
	# break

	minArgs = list(returnminArgs(distMatrix,clusteredPoints))
	print(minArgs)
	clusteredPoints = combine(clusteredPoints,minArgs)
	print(*clusteredPoints)

p = linkage(np.array(clusteredPoints), 'single')
fig = plt.figure(figsize = (2.5*(nosOfPoints+2), nosOfPoints+2))
dn = dendrogram(p)
