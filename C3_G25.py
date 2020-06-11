import math
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import plotly.figure_factory as ff

#Function to find minimum arguments of a 2D array
def returnminArgs(arr, pointsID):
	minD = sys.maxsize
	for i in range(len(arr)):
		for j in range(i):
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
		distanceBetweenPoints[i][j] = math.sqrt((matrixOfPoints[i][0]-matrixOfPoints[j][0])**2+(matrixOfPoints[i][1]-matrixOfPoints[j][1])**2)

clusteredPoints = pointID

while len(clusteredPoints) != 1:
	#Initialization of distance matrix
	distMatrix = [ [0]*len(clusteredPoints) for i in range(len(clusteredPoints)) ]
	for i in range(len(clusteredPoints)):
		distMatrix[i][i] = 0


	for i in range(len(clusteredPoints)):
		for j in range(len(clusteredPoints)):
			if i==j:
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

	minArgs = list(returnminArgs(distMatrix,clusteredPoints))
	clusteredPoints = combine(clusteredPoints,minArgs)

X = np.array(matrixOfPoints)

linked = linkage(X, 'single')

labelList = range(1, 11)

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            distance_sort='ascending',
            show_leaf_counts=True)
plt.show()